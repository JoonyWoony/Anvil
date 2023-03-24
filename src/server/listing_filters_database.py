# from anvil.tables import app_tables
for row in app_tables.database_name.search():
    print(row["Name"]) #Gets a specific row in the database, from the database called Database_Name
    # once run, this code will print every name that was inserted within the database.