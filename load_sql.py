import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

#  Correct path of database
db_path = r'C:\Users\saksh\OneDrive\Desktop\.database\sales_data.db' 

if not os.path.exists(db_path):
    print(" Database file NOT found", db_path)
    exit()
else:
    print(" Database file found")

#  Connect to the database
conn = sqlite3.connect(db_path)

# available tables
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(" Tables in DB:", tables)

#  SQL query on 'superstore' table
query = """
select
    product, 
    SUM(quantity) AS total_quantity, 
    SUM(quantity * price) AS revenue 
from  superstore 
group by  product;
"""

#  query and  DataFrame
try:
    df = pd.read_sql_query(query, conn)
    print("\n Query successful! Here's your data:\n")
    print(df)
except Exception as e:
    print("\n Error executing query:")
    print(e)

conn.close()


print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
