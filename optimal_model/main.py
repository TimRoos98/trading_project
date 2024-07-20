import numpy as np
import pandas as pd

# Configurable parameters
largestPositionMW = 30
orderCost = 0
minOrderSizeMW = 10
maxOrderSizeMW = 10
orderSizeJumps = 10
penalty_per_open_contract = 30

# Define the state space
stateRange = np.arange(-largestPositionMW, largestPositionMW + 1, orderSizeJumps)
actionRange = np.arange(-maxOrderSizeMW, maxOrderSizeMW + 1, minOrderSizeMW)

# Create dictionaries to map states and actions to their indices
state_to_index = {state: idx for idx, state in enumerate(stateRange)}
action_to_index = {action: idx for idx, action in enumerate(actionRange)}

# Define penalties for each state, using the penalty_per_open_contract
penalties = {
    0: 3 * penalty_per_open_contract,
    1: 2 * penalty_per_open_contract,
    2: penalty_per_open_contract,
    3: 0,
    4: penalty_per_open_contract,
    5: 2 * penalty_per_open_contract,
    6: 3 * penalty_per_open_contract
}

def GetContractPrice(time):
    return trades_df.loc[time, 'price']

def export_best_actions_to_csv(best_actions, filename):
    rows = []
    for time_idx, actions in enumerate(best_actions):
        for state, best_action in actions.items():
            rows.append({'time_index': time_idx, 'state': state, 'best_action': best_action})

    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)

def calculate_state_action_values(trades_df: pd.DataFrame):
    num_times = len(trades_df)
    value_map = [{} for _ in range(num_times)]

    # Initialize the cost-to-go matrix
    cost_to_go = np.full((num_times, len(stateRange)), float('inf'))

    # Iterate from the end to the start
    for time_idx in reversed(range(num_times)):
        price_per_mw = trades_df.loc[time_idx, 'price']
        time_map = {}

        for state in stateRange:
            state_idx = state_to_index[state]
            action_cost_map = {}

            for action in actionRange:
                resulting_state = state + action
                if resulting_state in stateRange:
                    resulting_state_idx = state_to_index[resulting_state]
                    future_cost = cost_to_go[time_idx + 1, resulting_state_idx] if time_idx < num_times - 1 else 0
                    total_cost = action * price_per_mw + future_cost
                    if action != 0:
                        total_cost += orderCost
                    action_cost_map[action_to_index[action]] = total_cost

            time_map[state_idx] = action_cost_map

            min_cost = min(action_cost_map.values(), default=float('inf'))
            cost_to_go[time_idx, state_idx] = min_cost

        # Debugging output
        print(f"Time index {time_idx}:")
        print(f"Time map: {time_map}")
        print(f"Cost to go: {cost_to_go[time_idx]}")

        value_map[time_idx] = time_map

    # Apply penalties for open contracts at the end of the period
    final_time_idx = num_times - 1
    for state, state_idx in state_to_index.items():
        if cost_to_go[final_time_idx, state_idx] < float('inf'):
            cost_to_go[final_time_idx, state_idx] += penalties.get(state, 0)

    return value_map, cost_to_go

def determine_best_actions(value_map):
    best_actions = []

    for time_idx, state_map in enumerate(value_map):
        best_action_for_state = {}

        for state, actions in state_map.items():
            best_action = None
            best_cost = float('inf')

            for action_idx, cost in actions.items():
                action = actionRange[action_idx]
                if cost < best_cost:
                    best_cost = cost
                    best_action = action

            best_action_for_state[state] = best_action

        best_actions.append(best_action_for_state)

    return best_actions

# Main script
if __name__ == '__main__':
    # Load trades DataFrame
    trades_df = pd.read_csv('../data/Trade_data_2024_05_10_14_00_00[85] (2).csv').drop(columns=['Unnamed: 0'])

    # Calculate state-action values and costs-to-go
    value_map, cost_to_go = calculate_state_action_values(trades_df)

    # Determine the best action for each state at each time point
    best_actions = determine_best_actions(value_map)

    # Export best actions to a CSV file
    export_best_actions_to_csv(best_actions, 'best_actions.csv')
