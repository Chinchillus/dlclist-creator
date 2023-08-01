import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedStyle

def create_dlclist_txt(directory_path):
    dlclist_path = os.path.join(directory_path, "dlclist.txt")
    try:
        with open(dlclist_path, "w") as file:
            for folder_name in os.listdir(directory_path):
                if os.path.isdir(os.path.join(directory_path, folder_name)):
                    file.write(f"\t\t<Item>dlcpacks:/{folder_name}/</Item>\n")
        return dlclist_path
    except Exception as e:
        return str(e)

def select_directory():
    directory_path = filedialog.askdirectory(title="Select Directory")
    if directory_path:
        result = create_dlclist_txt(directory_path)
        if result.startswith("Errno"):
            status_label.config(text=f"Error: {result}")
        else:
            status_label.config(text=f"dlclist.txt created at the folder that you selected", justify='center', anchor='center')
            open_dlclist(result)

def open_dlclist(file_path):
    try:
        if os.name == 'nt':  # Check if running on Windows
            os.startfile(file_path)
        elif os.name == 'posix':  # Check if running on Linux or macOS
            subprocess.run(["xdg-open", file_path], check=True)
    except Exception as e:
        print(f"Error opening dlclist.txt: {e}")

# Create the main window
app = tk.Tk()
app.title("dlclist creator")
app.resizable(False, False)
app.geometry("350x145")  # Increased height to accommodate the author label

# Set the dark theme using ttk styles
style = ThemedStyle(app)
style.set_theme("equilux")

# Set the background color of the main window
app.configure(bg="#1c1c1c")

# Customize the theme for all the widgets
style.configure(".", background="#1c1c1c", foreground="#FFFFFF")

# Create widgets with the ttk theme
instructions_label = ttk.Label(
    app, text="Select a directory containing the folders for the dlcpacks:")
instructions_label.pack(pady=10)

select_button = ttk.Button(app, text="Select Directory", command=select_directory)
select_button.pack(pady=5)

status_label = ttk.Label(app, text="")
selected_directory_label = ttk.Label(app, text="")
status_label.pack(pady=10)
selected_directory_label.pack(pady=5)

# Add the author label at the bottom
author_label = ttk.Label(app, text="Author: chinchill (Discord) please do not reupload, thank you")
author_label.pack(pady=5)
author_label.place(x=12, y=120) #162

app.mainloop()
