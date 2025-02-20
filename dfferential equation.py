from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

# Assuming 'data' contains the dataset and a column 'individual_id' exists to filter by a specific individual.
# We will simulate filtering for an individual with a hypothetical 'individual_id'
data['individual_id'] = 'A01'  # Simulate adding an 'individual_id' for demonstrative purposes
data_a01 = data[data['individual_id'] == 'A01']

# Check if there is enough data to proceed
if data_a01.empty:
    print("Error: No data available for the individual 'A01'. Check the dataset or filtering logic.")
else:
    # Define the heart rate model
    def heart_rate_model(H, t, k, H_rest):
        dHdt = -k * (H - H_rest)
        return dHdt

    # Initial conditions and time points
    H0 = data_a01['heart_rate'].iloc[0]  # Initial heart rate
    t = np.arange(0, len(data_a01))  # Time series
    k = 0.1  # Decay constant
    H_rest = 80  # Resting heart rate

    # Solving the differential equation
    H_solution = odeint(heart_rate_model, H0, t, args=(k, H_rest))

    # Plotting the results
    plt.figure(figsize=(12, 6))
    plt.plot(data_a01['timestamp'], data_a01['heart_rate'], label='Real Data')
    plt.plot(data_a01['timestamp'], H_solution, label='Model Prediction', linestyle='--')
    plt.title("Heart Rate Dynamics: Differential Equation Model")
    plt.xlabel("Time")
    plt.ylabel("Heart Rate (BPM)")
    plt.legend()
    plt.show()
