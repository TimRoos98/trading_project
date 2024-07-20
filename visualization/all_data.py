import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV file
forecast_df = pd.read_csv('../data/FR_ML_Forecasts_2024_05_10_14_00_00[4].csv').drop(columns=['Unnamed: 0'])
trades_df = pd.read_csv('../data/Trade_data_2024_05_10_14_00_00[85] (2).csv').drop(columns=['Unnamed: 0'])
forecast_df['published_at_utc'] = pd.to_datetime(forecast_df['published_at_utc'])
trades_df['execution_time'] = pd.to_datetime(trades_df['execution_time'])

fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot for trades data
sns.lineplot(data=trades_df, x='execution_time', y='price', marker='o', ax=ax1, color='b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Price', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_xticklabels(trades_df['execution_time'].dt.strftime('%Y-%m-%d %H:%M:%S'), rotation=45)

# Create a second y-axis for the forecast data
ax2 = ax1.twinx()
sns.lineplot(data=forecast_df, x='published_at_utc', y='value', marker='o', ax=ax2, color='r')
ax2.set_ylabel('Value', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Title and grid
plt.title('Trade Prices and Forecast Values Over Time')
fig.tight_layout()
plt.grid(True)

plt.show()


