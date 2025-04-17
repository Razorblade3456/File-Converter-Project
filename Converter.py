import tkinter as tk #this is the GUI library
from tkinterdnd2 import DND_FILES, TkinterDnD #This is for the Drag and Drop feature
from PIL import Image #For image processing
from tkinter import filedialog #Lets the user open file dialogs like "Save as"

dropped_image = None #this stores the image for later1

def handle_drop(event):
    global dropped_image  # We are using the global variable
    file_path = event.data.strip('{}')  # Get file path from dropped file
    try:
        dropped_image = Image.open(file_path)  # Save image globally
        dropped_image.save("output.png")  #Save a copy
        status_label.config(text="Saved as output.png!")  #Update message
        print("Image dropped and saved as output.png")  #Print for debug
    except Exception as e:
        status_label.config(text="Error opening image")
        print("Error:", e)


#this function runs when the save_button is clicked thru the command line
def save_file():
    global dropped_image #tells python to use the image we got from the drag and drop

    if dropped_image is None: #if no image was dropped yet
        status_label.config(text="Please drop an image first.")
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png", #If the user does not type .png at the end this adds it automatically
        filetypes=[("PNG files", "*.png"), #filters file types to only the ones shown
                   ("All files", "*.*")]
    )
    if file_path: #this makes it so if and when the user chooses a location, it saves it ot the chosen location
        dropped_image.save(file_path) #saves the image to the chosen path
        status_label.config(text="saved to {file_path}") #shows confirmation

#creating the GUI
root = TkinterDnD.Tk() #this is the main window with Drag and Drop support
root.title("Image dropper") #This is the Title of the window
root.geometry("400x400") #This sets the size of the window 

# Drop area
drop_label = tk.Label(root, text="Drop an image file here", bg="lightgray", width=40, height=10)
drop_label.pack(pady=20)
drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', handle_drop)

    
#creating the save button
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

#label to show messages
status_label = tk.Label(root, text="")
status_label.pack()

#starts the GUI loop
root.mainloop()