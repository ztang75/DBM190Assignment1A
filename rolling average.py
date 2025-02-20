
print("Columns available in data:", data.columns)

data_sorted = data.sort_values('timestamp')  # Sorting data by timestamp

data_sorted['heart_rate_rolling'] = data_sorted['heart_rate'].rolling(window=7).mean()

# Plotting the rolling heart rate
plt.figure(figsize=(12, 6))
plt.plot(data_sorted['timestamp'], data_sorted['heart_rate'], label='Raw Data', alpha=0.5)
plt.plot(data_sorted['timestamp'], data_sorted['heart_rate_rolling'], label='7-Hour Rolling Mean', color='red')
plt.title("Heart Rate Over Time (7-Hour Rolling Average)")
plt.xlabel("Time")
plt.ylabel("Heart Rate (BPM)")
plt.legend()
plt.show()
