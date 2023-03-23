# @anvil.server.callable
def get_fruit(fruit): 
  try: 
    get_data = app_tables.fruit_data.get(fruit_name=fruit) #fruit_data change to your database name, and fruit_name=fruit to the row and what you want to retrieve
    key = get_data['fruit'] #change 'decrypt_key' with the row_name that you want to retrieve
    return key #returns your final selected data.
  except Exception as e: 
    print(e) #returns error
 

# //Client Side
get_fruit('Apple')


#// Official Example
zaphod_row = app_tables.people.get(name="Zaphod Beeblebrox")
print(f"Zaphod is currently {zaphod_row['age']} years old")

# It's Zaphod's birthday, update the database
zaphod_row['age'] += 1