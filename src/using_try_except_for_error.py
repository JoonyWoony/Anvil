# You can use Try and Except in order to catch errors and prevent those errors from causing a fatal error, which would shut down the app.
#// EXAMPLE
try: #Try to execute the code below: 
    print('This worked!')
except: #failed to execute. so trigger this instead
    print('This failed.')

#Upon using try and except, you can also catch which error was triggered, and log into the console:
try:
    print('This Worked!')
except Exception as e: #stored Exception as e
    print(f'This failed as an error was triggered. Error: {e}') # {e} is the defined error variable above
# ?? You can replace the print() with alert() within anvil to cause an alert, and not log into console.

   