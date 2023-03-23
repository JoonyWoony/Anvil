# docs: https://anvil.works/docs/client/components/basic
#// Example 1 - Adding a label through button event 
def submit_button_click(self, **event_args): #as always replace submit_button_click with your button name
    label = Label(text='This is a text label.') #You can also change colour of the label, and other stuff, you can view in properties of label
    self.add_component(label) 
    # result: Upon button click, the label should be added to the app. If you want to add it to a specific panel:
    self.column_panel.add_component(label) #change column_panel to your column panel name
