import os
import sys

# -----------------------------------------
# ADD ROOT DIRECTORY TO PYTHON PATH
# -----------------------------------------

ROOT_DIR = os.path.abspath(
    os.path.dirname(__file__)
)

sys.path.insert(0, ROOT_DIR)

# -----------------------------------------
# IMPORTS
# -----------------------------------------

import pandas as pd

from src.database.mysql_connection import (
    connect_mysql
)

# -----------------------------------------
# CONNECT MYSQL
# -----------------------------------------

connection = connect_mysql()

print("MySQL Connected Successfully")

# -----------------------------------------
# EXECUTE QUERY
# -----------------------------------------

query = "SELECT * FROM customer_data LIMIT 10"

df = pd.read_sql(query, connection)

# -----------------------------------------
# DISPLAY DATA
# -----------------------------------------

print(df)

# -----------------------------------------
# CLOSE CONNECTION
# -----------------------------------------

connection.close()

print("Connection Closed")