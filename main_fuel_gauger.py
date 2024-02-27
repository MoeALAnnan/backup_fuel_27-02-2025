#!/usr/bin/python3
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import StringVar, IntVar
import classes
from page1 import create_new_frame, go_to_next_page, configure_text_kilo_or_livre
import frame_manager
from tkcalendar import DateEntry
from datetime import date
import pickle
from write import main
from customtkinter import *
window = CTk()
window.title("AIRBUS")
set_appearance_mode("dark")

ki_lo_var = IntVar()
frame = CTkFrame(master = window)
frame.pack()
#AirCraft information 
main_frame = CTkFrame(frame, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
main_frame.grid(row = 0, column = 0, padx=20, pady=10)
# Load the logo image
logo_path = r"C:\Users\Momo\Desktop\logo2.png"  # Modify this with the actual logo file name and extension
logo = Image.open(logo_path)
logo = logo.resize((100,100))
logo = ImageTk.PhotoImage(logo, size=(frame.winfo_width(), frame.winfo_height()))  # Adjust the size
#this is the 1st label frame will be used to display the logo
title_frame = tkinter.LabelFrame(main_frame)
title_frame.grid(row = 0, column = 0, sticky="news", padx=20)

# Create a label to display the logo
logo_label = tkinter.Label(title_frame, image=logo)
logo_label.grid(row=0, column=0)

# Configure the column and row weights so they expand proportionally
title_frame.grid_rowconfigure(0, weight=1)
title_frame.grid_columnconfigure(0, weight=1)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
####the title of the 2nd label frame 
user_info_frame = tkinter.LabelFrame(main_frame, text = "user information")
user_info_frame.grid(row = 1, column = 0, sticky= "news", padx=20, pady=10)


##### labels found inside user_info_frame

#MSN label and entry field
ac_msn_label = tkinter.Label(user_info_frame, text="MSN")
ac_msn_label.grid(row=0, column=0)
ac_msn_entry = tkinter.Entry(user_info_frame)
ac_msn_entry.grid(row=1, column=0)

#aircraft version label and entry field
ac_version_label = tkinter.Label(user_info_frame, text="Version")
ac_version_label.grid(row=0, column=1)
ac_version_entry= tkinter.Entry(user_info_frame)
ac_version_entry.grid(row =1, column=1)

#fqi part number and entry field
ac_fqi_part_label = tkinter.Label(user_info_frame, text="FQI P/N")
ac_fqi_part_label.grid(row=0, column=2)
ac_fqi_part_entry = tkinter.Entry(user_info_frame)
ac_fqi_part_entry.grid(row=1, column=2)

#fqi serial number label and entry field
ac_fqi_serial_label = tkinter.Label(user_info_frame, text="FQI S/N")
ac_fqi_serial_label.grid(row=2, column=0)
ac_fqi_serial_entry = tkinter.Entry(user_info_frame)
ac_fqi_serial_entry.grid(row=3, column=0)

#stamp label and entry field
ac_stamp_label = tkinter.Label(user_info_frame, text="Stamp")
ac_stamp_label.grid(row=2, column=1)
ac_stamp_entry= tkinter.Entry(user_info_frame)
ac_stamp_entry.grid(row =3, column=1)

#date label and entry field
today= date.today()

date_label = tkinter.Label(user_info_frame, text="Date")
date_label.grid(row=2, column=2)
date_entry = DateEntry(user_info_frame, date_pattern='dd/mm/yyyy', mindate=today, state="readonly")
date_entry.grid(row=3, column=2, padx=5, pady=5)

###########the title of the 3rd label frame 
engine_info_frame = tkinter.LabelFrame(main_frame, text = "Engine information")
engine_info_frame.grid(row = 2, column = 0, sticky="news", padx=20, pady=10)

##########Engine type label and entry field
ac_engine_label = tkinter.Label(engine_info_frame, text="Engine Type")
ac_engine_label.grid(row=0, column=0)
ac_engine_combobox = ttk.Combobox(engine_info_frame, values=["CFM", "PW1100G", "CFM"], state="readonly")
ac_engine_combobox.grid(row=1, column=0)

########## Create two check buttons, link them to the IntVar, and set their values

checkbutton1 = tkinter.Radiobutton(engine_info_frame, text="KILO", variable=ki_lo_var, value=1)
checkbutton1.grid(row=0, column=1)
checkbutton2 = tkinter.Radiobutton(engine_info_frame, text="LIVRE", variable=ki_lo_var, value=2)
checkbutton2.grid(row=0, column=2)



entry_manager = classes.EntryManager(ac_msn_entry, ac_version_entry, ac_fqi_part_entry, ac_fqi_serial_entry, ac_stamp_entry, date_entry, ac_engine_combobox, ki_lo_var)
frame_manager.created_frames.append(main_frame)
def on_start():
    if entry_manager.are_entries_filled():
        dictionary_page0 = entry_manager.handle_store_entries()
        with open('dictionary_page0.pkl', 'wb') as file:
            pickle.dump(dictionary_page0, file)
        create_new_frame(frame, next_page_button, start_button)
        configure_text_kilo_or_livre(ki_lo_var)
        error_label.config(text="")  # Clear any previous error message
        # hide_page1_frames()
        # entry_manager.reset_entries()
    else:
        error_label.configure(text="Error: Please fill in all the entries.")
        tkinter.messagebox.showerror("Error", "Please fill in all the entries.")
###########the title of the 4th label frame 
start_reset_frame = CTkFrame(main_frame, fg_color="#8D6F3A")
start_reset_frame.grid(row = 3, column = 0, sticky="news", padx=20, pady=20)

start_button = CTkButton(start_reset_frame, text="Start", command = on_start)
start_button.grid(row=0, column=0, padx=5)
error_label = CTkLabel(main_frame, text="")
error_label.grid(row=4, column=0, pady=(0, 10))


def on_reset(): 
    entry_manager.reset_entries()
    #erase_page1_entries()

def on_next_page_button():
    if entry_manager.are_entries_filled():
        entry_manager.handle_store_entries()
        dictionary_page0 = entry_manager.handle_store_entries()
        with open('dictionary_page0.pkl', 'wb') as file:
            pickle.dump(dictionary_page0, file)
        configure_text_kilo_or_livre(ki_lo_var)
        go_to_next_page()
        error_label.configure(text="")  # Clear any previous error message
        # hide_page1_frames()
        # entry_manager.reset_entries()
    else:

        error_label.configure(text="Error: Please fill in all the entries.")
        tkinter.messagebox.showerror("Error", "Please fill in all the entries.")


    
reset_button = CTkButton(start_reset_frame, text="Reset", command= on_reset)
reset_button.grid(row=0, column=2, padx=5)

next_page_button = CTkButton(start_reset_frame, text="Next Page", command=on_next_page_button)
next_page_button.grid(row=0, column=1)
next_page_button.configure(state=tkinter.DISABLED)  # Initially disabled


window.mainloop()