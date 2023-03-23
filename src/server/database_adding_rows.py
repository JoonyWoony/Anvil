# from anvil.tables import app_tables
#// Example
@anvil.server.callable
def data(data, key):
  try:  #change encrypted_data to your database name
    app_tables.encrypted_data.add_row(created=datetime.now(), decrypt_key=key, encrypted_content=data) #attempt to add row?
    return True
  except Exception as error: 
    print(f"An error occured while adding the data to the database, {error}")
    return False
# how to use app tables; https://anvil.works/docs/data-tables/data-tables-in-code