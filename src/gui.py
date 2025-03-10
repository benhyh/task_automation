# Import tkinter - it's like bringing a box of art supplies to build our app's window
import tkinter as tk
# Import ttk from tkinter - it's like getting extra fancy decorations for our art project
from tkinter import ttk

# Create a class called AutomationGUI - think of this as a blueprint for building a robot
# that will help us organize our tasks and files
class AutomationGUI:
    # This is what happens when we first build our robot
    def __init__(self, root):
        # The root is like the robot's body - it's the main window of our app
        self.root = root
        # This gives our robot a name tag that shows at the top of the window
        self.root.title("Task Automation Suite")
        # Now let's call another method to build all the controls for our robot
        self.setup_ui()
        
    # This method builds all the buttons and controls for our robot
    def setup_ui(self):
        # Create tabs - these are like different pages in a notebook
        # so we can organize different features
        self.tab_control = ttk.Notebook(self.root)
        
        # Create the first page in our notebook for managing tasks
        # It's like a blank piece of paper where we'll add buttons later
        self.task_tab = ttk.Frame(self.tab_control)
        
        # Create the second page for managing files
        # Another blank piece of paper for a different topic
        self.file_tab = ttk.Frame(self.tab_control)
        
        # Add our pages to the notebook with labels
        # This is like putting a sticky note on each page so we know what it's for
        self.tab_control.add(self.task_tab, text="Tasks")
        self.tab_control.add(self.file_tab, text="File Management")
        
        # Put the notebook in our main window and make it fill the space
        # This is like gluing our notebook onto the robot so it's always visible
        # expand=1 means it grows when the window grows (like a sponge in water)
        # fill="both" means it fills in both directions (like water filling a container)
        self.tab_control.pack(expand=1, fill="both")