# 选择需要统计的参数列
params = ['activity_freq', 'movement_distance', 'heart_rate', 'energy_expenditure']

# 计算均值、中位数、标准差、方差
stats = data[params].agg(['mean', 'median', 'std', 'var']).T
stats.columns = ['Mean', 'Median', 'Standard Deviation', 'Variance']
print("基础统计量：")
print(stats)
