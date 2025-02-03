import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
file_path = r'C:/Users/sharm/Downloads/2025-01-29 Modern Bhatti june-month_ vegetables prices(Sheet1).csv'
df = pd.read_csv(file_path)

# Step 2: Rename columns for better readability
# The first column is 'Vegetables', and the rest are dates
new_column_names = ['Vegetables']  # Start with 'Vegetables' as the first column name

# Extracting date part from column names and adding them to the list
for col in df.columns[1:]:  # Skip the first column
    new_column_names.append(col.split(":")[1])  # Extract date part

df.columns = new_column_names  # Rename columns

# Step 3: Remove the first row (it contains extra labels)
df = df.iloc[1:].reset_index(drop=True)  # Remove first row and reset index

# Step 4: Convert all prices to numeric values
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Step 5: Set 'Vegetables' as the index
df.set_index('Vegetables', inplace=True)

# Step 6: Transpose the data (switch rows and columns)
df_transposed = df.T  # Now dates are rows, and vegetables are columns

# Step 7: Calculate daily price change
price_change = df_transposed.diff()  # Difference between consecutive days

# Step 8: Plot price trends
plt.figure(figsize=(12, 6))  # Set figure size

for vegetable in df.index:  # Loop through each vegetable
    plt.plot(df_transposed.index, df_transposed[vegetable], marker='o', linestyle='-', label=vegetable)

# Step 9: Customize the plot
plt.xlabel("Date")  # Label for x-axis
plt.ylabel("Price per kg (Rs)")  # Label for y-axis
plt.title("Vegetable Price Trends")  # Title of the graph
plt.xticks(rotation=45)  # Rotate date labels for better visibility
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Show legend outside the graph
plt.grid(True)  # Add grid for better readability

# Step 10: Show the plot
plt.show()

# Step 11: Print exact price changes
print("Exact Price Changes:")
print(price_change)