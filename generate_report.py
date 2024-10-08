import pandas as pd

# Define sample data
data = {
    "Date": ["2024-08-01", "2024-08-05", "2024-08-12"],
    "Description": ["Deposit", "Grocery Store", "Utility Bill"],
    "Amount": [500, -50, -75],
    "Balance": [500, 450, 375]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('bank_statement_report.csv', index=False)

# Print confirmation message
print("Bank statement report generated and saved as 'bank_statement_report.csv'.")
