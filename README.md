# Task_7-sqlite
# Sales Analysis

## Description
This project performs data analysis on sales data to generate visualizations and insights about product performance.

## Files
- `load_sql.py`: Python code for data analysis and creating charts.
- 'sales_data.db' : sqlite file (raw data)
- `sales_data.csv`: Sales data used for analysis.

## Requirements
- Python 3.x
- pandas
- matplotlib
- sqlite3
  

## Key Features
- **Data Analysis**: Summarizes sales data by product, category, and region.
- **Visualizations**: Generates charts to visualize sales performance (e.g., revenue per product).
- **SQL Database**: Data is stored and managed in an SQLite database.

## python code
1. Pie chart
print(df)
# Pie Chart 
plt.figure(figsize=(8,8))  # You can adjust the size of the chart
plt.pie(df['revenue'], labels=df['product'], autopct='%1.1f%%', startangle=90)
plt.title("Revenue Distribution by Product") 
plt.axis('equal') 
plt.show()

2. Bar chart
print(df)
# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
