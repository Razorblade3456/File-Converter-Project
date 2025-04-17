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
        filetypes=[("PNG files", "*.png"), #filters file types to only the ones shown (png, jpg, bmp and gif files)
                   ("JPEG files", "*.jpg;*jpeg"),
                   ("Bitmap files", "*.bmp"),
                   ("GIF files", "*.gif"),
                   ("All files", "*.*")]
    )
    if file_path: #this makes it so if and when the user chooses a location, it saves it ot the chosen location
        dropped_image.save(file_path) #saves the image to the chosen path
        status_label.config(text="saved to {file_path}") #shows confirmation


#creating a resize option
def resize_option():
    global dropped_image #This is to use the Image that we already dropped

    if dropped_image is None: #if no image is dropped then the status label config happens
        status_label.config(text="Please drop an image to resize first.")
        return
    
    try: 
        #this gets the width and height entered by the users in the text boxes
        new_width = int(width_entry.get()) #This converts the text number into a number (interger)
        new_height = int(height_entry.get()) #this does the same thing as the line above but for height

        #resizing the image using PIL
        dropped_image = dropped_image.resize((new_width, new_height)) #this allows the user to resize the image

        status_label.config(text="Image resized to {new_width}x{new_height}") #this is the updated text that appears when the image is resized
        print("resized image:", new_width, new_height) #this debugs print
    except Exception as e:
        status_label.config(text="Resize failed :(") #this is for the error message the pops up if something were to go wrong
        print("Resize error:", e) #prints the error in the console


#creating the GUI
root = TkinterDnD.Tk() #this is the main window with Drag and Drop support
root.title("Image dropper") #This is the Title of the window
root.geometry("500x500") #This sets the size of the window 

#adding labels and input boxes for width and height resize
tk.Label(root, text="Width:").pack() #this is the label for width
width_entry = tk.Entry(root) #this is for the input box for width
width_entry.pack() #this line of code is what allows us to see it on the screen

tk.Label(root, text="Height:").pack() #this is the label for height
height_entry = tk.Entry(root) #this is the input box for height
height_entry.pack() #this line of code is what allows us to see it on the screen

#adding the button to initiate the resize option
resize_button = tk.Button(root, text="Resize Image", command=resize_option)
resize_button.pack()

# Drop area
drop_label = tk.Label(root, text="Drop an image file here", bg="lightblue", width=40, height=20)
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