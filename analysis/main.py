import pandas as pd

action_ratio = 0.1
actions = 7
actionCost = 0
penalty_per_open_contract = 30
penalties = {
    0: 3 * penalty_per_open_contract,
    1: 2 * penalty_per_open_contract,
    2: penalty_per_open_contract,
    3: 0,
    4: penalty_per_open_contract,
    5: 2 * penalty_per_open_contract,
    6: 3 * penalty_per_open_contract
}



def load_best_actions(filename):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)
    return df


def get_action_for_state_at_time(df, time_index, state):
    # Filter the DataFrame for the given time_index and state
    filtered_df = df[(df['time_index'] == time_index) & (df['state'] == state)]

    # Get the action(s) for the specified time index and state
    if not filtered_df.empty:
        action = filtered_df['best_action'].values[0]
        return action
    else:
        return None


def get_action_sequence(df, initial_state, start_time_index, num_time_steps):
    state = initial_state
    current_time_index = start_time_index
    action_sequence = []

    for time in range(num_time_steps):
        # Get the best action for the current state at the current time index
        action = get_action_for_state_at_time(df, current_time_index, state)

        if action is not None:
            # Append the time index, state, and action to the sequence
            action_sequence.append({
                'time_index': current_time_index,
                'state': state,
                'action': action
            })

            # Update the state based on the action taken
            state += action * action_ratio

            # Move to the next time index
            current_time_index += 1
        else:
            # If no action is found, stop the sequence
            break

    return action_sequence


def compute_total_actions_and_profit(action_sequence, trades_df):
    total_actions = 0
    total_profit = 0.0
    total_actions = sum(1 for entry in action_sequence if entry['action'] != 0)
    costs = total_actions * actionCost
    penalty = penalties.get(action_sequence[-1]['state'])
    print(total_actions)
    for index, row in trades_df.iterrows():
        total_profit += row['price'] * action_sequence[index]['action']

    print(f"total profit = {total_profit - costs - penalty}")
    print(f"total actions = {total_actions} ")





if __name__ == '__main__':
    # Load best actions from the CSV file
    filename = '../optimal_model/best_actions.csv'
    best_actions_df = load_best_actions(filename)

    # Define the starting state, initial time index, and number of time steps
    initial_state = 4
    start_time_index = 0
    num_time_steps = (len(best_actions_df) // actions)  # Number of time steps to simulate
    print(f"Number of time steps: {num_time_steps}")

    # Get the action sequence
    action_sequence = get_action_sequence(best_actions_df, initial_state, start_time_index, num_time_steps)

    # Output the result


    # Load trades DataFrame to calculate profit
    trades_df = pd.read_csv('../data/Trade_data_2024_05_10_14_00_00[85] (2).csv').drop(columns=['Unnamed: 0'])
    compute_total_actions_and_profit(action_sequence, trades_df)
    # # Compute total actions and profit
    # total_actions, total_profit = compute_total_actions_and_profit(action_sequence, trades_df)
    #
    # print(f"Total Actions: {total_actions}")
    # print(f"Total Profit: {total_profit}")
