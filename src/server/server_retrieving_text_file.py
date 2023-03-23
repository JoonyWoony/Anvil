
# from anvil.files import data_files
# import data files service
# @anvil.server.callable  [This must always be above a server function] 
def read_text(txt):
    try: 
        with open(data_files[f'{txt}']) as f:
            text = f.read()
            return text
    except Exception as error:
        print(error)
        return False
# //Example 
content = read_text('text_file.txt')
print(content)
# if the text file.txt exists within data files, it will read the contents then print through console