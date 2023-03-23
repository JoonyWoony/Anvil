##// https://anvil.works/docs/client/components/basic for text box name

def clear_inputs(self):
    self.name_box.text = ""
    # change name_box to the text box that you want to clear
def submit_button_click(self, **event_args): #You must change submit_button_click to your button event handler in order for it to work
    self.clear_inputs() #mentioning the function to clear the text box upon button click event is triggered.
    #clears the input in the textbox that you specified