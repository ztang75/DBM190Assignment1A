import pandas as pd
import numpy as np

# 设置随机种子
np.random.seed(42)

# 生成时间戳（7天，每小时）--> 使用小写 "h"
timestamps = pd.date_range(start="2024-06-01", end="2024-06-07", freq="h")
n = len(timestamps)
individuals = ["A01", "A02", "A03"]

# 初始化DataFrame
data = pd.DataFrame({
    "timestamp": np.tile(timestamps, len(individuals)),
    "individual_id": np.repeat(individuals, n)
})

# 生成参数（基于逻辑关系）
def generate_parameters(df):
    # 活动频率（白天高，夜间低）
    hour = df["timestamp"].dt.hour
    df["activity_freq"] = np.clip(
        15 + 10 * np.sin(2 * np.pi * (hour - 6) / 24) + np.random.normal(0, 3, len(df)),
        0, 30
    ).round(1)
    
    # 移动距离（与活动频率正相关）
    df["movement_distance"] = np.clip(
        df["activity_freq"] * 30 + np.random.normal(0, 50, len(df)),
        0, 1000
    ).round(1)
    
    # 心率（随活动频率升高）
    df["heart_rate"] = np.clip(
        80 + df["activity_freq"] * 3 + np.random.normal(0, 10, len(df)),
        80, 180
    ).round(0)
    
    # 体温（正常波动）
    df["body_temp"] = np.clip(
        37 + 0.1 * df["activity_freq"] + np.random.normal(0, 0.5, len(df)),
        36, 40
    ).round(1)
    
    # 能量消耗（公式计算）
    df["energy_expenditure"] = np.clip(
        50 + df["activity_freq"] * 10 + np.random.normal(0, 20, len(df)),
        50, 500
    ).round(1)
    
    # 环境参数
    df["habitat_temp"] = np.clip(
        25 + 10 * np.sin(2 * np.pi * (hour - 12) / 24) + np.random.normal(0, 2, len(df)),
        10, 35
    ).round(1)
    
    df["light_intensity"] = np.clip(
        5000 * np.sin(2 * np.pi * (hour - 6) / 24) + np.random.normal(0, 1000, len(df)),
        0, 10000
    ).round(0)
    
    return df

# 添加 include_groups=False 避免警告
data = data.groupby("individual_id", group_keys=False).apply(generate_parameters, include_groups=False)

# 保存数据并打印前5行
data.to_csv("golden_monkey_data.csv", index=False)
print("数据已保存为 golden_monkey_data.csv！")
print("\n前5行数据预览：")
print(data.head())