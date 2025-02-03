import pandas as pd
import matplotlib.pyplot as plt

# Extracted data
data = {
    "Vegetable Name": [
        "Akabare Chilly", "Beetroot", "Bitter Gourd", "Brinjal", "Broccoli", "Cabbage", "Cabbage Red",
        "Capsicum", "Carrot", "Cauliflower", "Cucumber Hybrid", "Fresh Green Peas", "Garlic",
        "Green Beans", "Green Chilly", "Lemon", "Mushroom Button", "Okra", "Onion", "Potato",
        "Radish", "Salad Tomato", "Tomato", "Tomato Hybrid"
    ],
    "Price": [87.5, 60, 60, 70, 50, 50, 80, 60, 120, 40, 100, 140, 290, 40, 30, 130, 150, 65, 80, 50, 40, 100, 50, 100],
    "Price on our web": [115, 50, 80, 90, 130, 60, 140, 110, 145, 70, 115, 220, 437, 72, 28, 160, 230, 78, 170, 92, 69.3, 160, 85, 115]
}

# Convert to DataFrame
df = pd.DataFrame(data)



# Plotting
plt.figure(figsize=(12, 6))
x = range(len(df))

plt.bar(x, df["Price"], width=0.4, label="Price", align="center", color='b', alpha=0.6)
plt.bar([i + 0.4 for i in x], df["Price on our web"], width=0.4, label="Price on our web", align="center", color='r', alpha=0.6)

plt.xticks([i + 0.2 for i in x], df["Vegetable Name"], rotation=90)
plt.ylabel("Price in market (in currency units)")
plt.title("Comparison of Market Price vs Web Price of Vegetables")
plt.legend()
plt.tight_layout()
# Show plot
plt.show()
