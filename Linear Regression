# 提取变量
X = data[['activity_freq']]  # 自变量：活动频率
y = data['energy_expenditure']  # 因变量：能量消耗

# 训练模型
model = LinearRegression()
model.fit(X, y)

# 预测值
y_pred = model.predict(X)

# 绘制回归线
plt.figure(figsize=(10, 6))
sns.scatterplot(x='activity_freq', y='energy_expenditure', data=data, alpha=0.5)
plt.plot(X, y_pred, color='red', linewidth=2, label=f"Regression Line (R²={model.score(X, y):.2f})")
plt.title("Linear Regression: Activity Frequency vs. Energy Expenditure")
plt.xlabel("Activity Frequency (counts/min)")
plt.ylabel("Energy Expenditure (kcal/hour)")
plt.legend()
plt.show()
