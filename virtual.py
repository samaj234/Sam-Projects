import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
# 1. Dataset
x = np.array([1000, 1500, 2000])  # House sizes
y = np.array([300, 400, 500])     # Prices

# 2. Initialize parameters
m = 0  # Slope
b = 0  # Intercept
learning_rate = 0.0000001
iterations = 1000

# 3. Define the loss function
def compute_loss(x, y, m, b):
    """
    Compute Mean Squared Error (MSE).
    """
    y_pred = m * x + b
    return np.mean((y - y_pred) ** 2)

# 4. Gradient Descent Algorithm
for i in range(iterations):
    # Compute predictions
    y_pred = m * x + b
    
    # Compute gradients
    dm = -2 * np.mean(x * (y - y_pred))  # Derivative w.r.t. m
    db = -2 * np.mean(y - y_pred)       # Derivative w.r.t. b
    
    # Update parameters
    m -= learning_rate * dm
    b -= learning_rate * db

    # Print loss every 100 iterations
    if i % 100 == 0:
        loss = compute_loss(x, y, m, b)
        print(f"Iteration {i}: Loss = {loss:.2f}, m = {m:.4f}, b = {b:.4f}")

# Final results
print("\nFinal values:")
print(f"m (slope): {m}")
print(f"b (intercept): {b}")


# Generate a random 5D dataset (5 features)
np.random.seed(42)
X = np.random.rand(100, 5)  # 100 samples, 5 features

# Apply PCA to reduce dimensions to 2
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Plot the reduced data (2D visualization)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], color='blue')
plt.title("2D Visualization of 5D Data after PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()
