# //Clearing components
# // first locate the base self name, meaning locate the name of the column panel etc.
self.column_panel.clear() #change column_panel to your own, and this will clear all the components that were added, except the ones you added manually through the panel.
self.column_panel.add_component() #add label 
# You can add your own label here, which will do something like this: 
# 1. Clears all the components that were added
# 2. then readds the specified label, this can be used for displaying labels, but not duplicating them below.