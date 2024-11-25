# import duckdb

# # Connect to DuckDB (in-memory)
# # conn = duckdb.connect()

# # # Read the CSV file into a DuckDB table
# # conn.execute("CREATE TABLE data AS SELECT * FROM read_csv_auto('data.csv')")

# # # Query the data with random ordering and store in a Pandas DataFrame
# # df = conn.execute("SELECT * FROM data ORDER BY RANDOM()").df()

# # # Display the DataFrame in Streamlit
# # st.table(df)

# # # Close the connection
# # conn.close()

# # result = duckdb.sql("SELECT DISTINCT Subcategory FROM 'data.csv'").fetchall()
# # result = duckdb.sql("SELECT COUNT(*) FROM 'data.csv'").fetchall()
# category = "Verbes"
# #result = duckdb.sql("SELECT * FROM 'data.csv' WHERE Category = ? ", (category,))#.fetchall()
# query = "SELECT * FROM 'data.csv' WHERE Category = ?", (category, )
# print(query)
# # result = duckdb.sql("""SELECT * FROM 'data.csv' WHERE Category = ? """, (category,)).fetchall()

# # print(result)

import duckdb
import pandas as pd
import time

# Connect to DuckDB (in-memory)
start_time = time.time()
conn = duckdb.connect()
end_time = time.time()
print(f"Connection time: {end_time - start_time:.4f} seconds")

# Read the CSV file into a DuckDB table
start_time = time.time()
conn.execute("CREATE TABLE data AS SELECT * FROM read_csv_auto('data.csv')")
end_time = time.time()
print(f"CSV loading time: {end_time - start_time:.4f} seconds")

category = "Verbes"

# Execute the query and measure time
start_time = time.time()
result = conn.execute("SELECT * FROM data WHERE Category = ? ORDER BY RANDOM()", (category,)).fetchall()
end_time = time.time()
print(f"Query execution time: {end_time - start_time:.4f} seconds")

# Convert to Pandas DataFrame and measure time (if needed)
start_time = time.time()
df = pd.DataFrame(result)  # If you need a DataFrame
end_time = time.time()
print(f"DataFrame conversion time: {end_time - start_time:.4f} seconds")

# Print the first few rows of the result (optional)
print(df.head())

# Close the connection


start_time = time.time()
res = duckdb.sql("SELECT * from 'data.csv'").fetchall()
end_time = time.time()
print(f"Duckdbsql time: {end_time - start_time:.4f} seconds")
print(res)


conn.close()