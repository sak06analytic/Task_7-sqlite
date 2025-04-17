import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# ✅ STEP 1: Correct path to your database
db_path = r'C:\Users\saksh\OneDrive\Desktop\.database\sales_data.db'  # ← Make sure this file is really here!

# ✅ STEP 2: Check if the file exists
if not os.path.exists(db_path):
    print("❌ Database file NOT found at:", db_path)
    exit()
else:
    print("✅ Database file FOUND!")

# ✅ STEP 3: Connect to the database
conn = sqlite3.connect(db_path)

# ✅ STEP 4: Optional - Show available tables
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("📋 Tables in DB:", tables)

# ✅ STEP 5: SQL query on 'superstore' table
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM 
    superstore 
GROUP BY 
    product;
"""

# ✅ STEP 6: Run the query and load into DataFrame
try:
    df = pd.read_sql_query(query, conn)
    print("\n✅ Query successful! Here's your data:\n")
    print(df)
except Exception as e:
    print("\n❌ Error executing query:")
    print(e)

# ✅ STEP 7: Close connection
conn.close()


print(df)

# ✅ Plot bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
