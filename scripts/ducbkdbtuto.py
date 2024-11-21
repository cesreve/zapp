import duckdb
import pandas as pd

# # create a connection to a file called 'file.db'
# con = duckdb.connect("file.db")
# # create a table and load data into it
# con.sql("CREATE TABLE IF NOT EXISTS test (i INTEGER)")
# con.sql("INSERT INTO test VALUES (42)")
# # query the table
# #print(con.table("test").show())
# # explicitly close the connection
# con.close()

#print(duckdb.sql("SELECT 42").df() )


# pandas_df = pd.DataFrame({"a": [42]})
# dtf = duckdb.sql("SELECT * FROM pandas_df")
# print(dtf)




# Create a Pandas dataframe
my_df = pd.DataFrame.from_dict({'a': [42]})

# query the Pandas DataFrame "my_df"
# Note: duckdb.sql connects to the default in-memory database connection
results = duckdb.sql("SELECT * FROM my_df").df()
print(results.head().shape)
print(results.head().dtypes)