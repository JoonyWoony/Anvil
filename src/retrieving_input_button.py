def submit_button_click(self, **event_args): #change submit_button_click to your button event handler
    text_box = self.text_box.txt #change text_box to your text_box.  This line of code will retrieve the input from the user.
    #// text box name can be seen in the name category in your properties: https://anvil.works/docs/client/components/basic
    print(text_box)
    # Using text_box variable, you can do anything with the input that you obtained.