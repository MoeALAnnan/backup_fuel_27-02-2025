#!/usr/bin/python3
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import StringVar, IntVar
import classes
import classes_page1
import page1
from page1 import create_new_frame, go_to_next_page, configure_text_kilo_or_livre, erase_page1_entries
import page2
from page2 import erase_page2_entries, destroy_second_frame
import frame_manager
from tkcalendar import DateEntry
from datetime import date
import pickle
from write import main
from customtkinter import *

import tkinter as tk



window = CTk()
window.title("FuelCulator 1.0")
set_appearance_mode("light")

ki_lo_var = IntVar()
frame = CTkFrame(master = window)
frame.pack()
#AirCraft information 
main_frame = CTkFrame(frame,fg_color="#003554", border_color="black", border_width=1)
main_frame.grid(row = 0, column = 0, padx=2, pady=2)
# Load the logo image
logo_path = r"C:\Users\Momo\Desktop\bg_2.png"  # Modify this with the actual logo file name and extension
logo = Image.open(logo_path)
logo = logo.resize((150,150))
logo = ImageTk.PhotoImage(logo)  # Adjust the size
#this is the 1st label frame will be used to display the logo
title_frame = CTkFrame(main_frame, fg_color="#006494", border_color="#3a7ca5", border_width=2)
title_frame.grid(row = 0, column = 0, padx=5, pady=10)

# Create a label to display the logo
logo_label = tkinter.Label(title_frame, image=logo, background="#003554",text="")
logo_label.grid(row=0, column=0)

# Configure the column and row weights so they expand proportionally
title_frame.grid_rowconfigure(0, weight=1)
title_frame.grid_columnconfigure(0, weight=1)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
####the title of the 2nd label frame 
user_info_frame = CTkFrame(main_frame,fg_color="#006494", border_color="#3a7ca5", border_width=2)
user_info_frame.grid(row = 1, column = 0, sticky= "news", padx=5, pady=20)


##### labels found inside user_info_frame

#MSN label and entry field
ac_msn_label = CTkLabel(user_info_frame, text="MSN")
ac_msn_label.grid(row=0, column=0, padx=5, pady=5)
ac_msn_entry = CTkEntry(user_info_frame)
ac_msn_entry.grid(row=1, column=0, padx= 5)

#aircraft version label and entry field
ac_version_label = CTkLabel(user_info_frame, text="Version")
ac_version_label.grid(row=0, column=1, padx=5, pady=5)
ac_version_entry= CTkEntry(user_info_frame)
ac_version_entry.grid(row =1, column=1, padx=5)

#fqi part number and entry field
ac_fqi_part_label = CTkLabel(user_info_frame, text="FQI P/N")
ac_fqi_part_label.grid(row=0, column=2, padx=5, pady=5)
ac_fqi_part_entry = CTkEntry(user_info_frame)
ac_fqi_part_entry.grid(row=1, column=2, padx= 5)

#fqi serial number label and entry field
ac_fqi_serial_label = CTkLabel(user_info_frame, text="FQI S/N")
ac_fqi_serial_label.grid(row=2, column=0, padx=5, pady=5)
ac_fqi_serial_entry = CTkEntry(user_info_frame)
ac_fqi_serial_entry.grid(row=3, column=0)

#stamp label and entry field
ac_stamp_label = CTkLabel(user_info_frame, text="Stamp")
ac_stamp_label.grid(row=2, column=1, padx=5, pady=5)
ac_stamp_entry= CTkEntry(user_info_frame)
ac_stamp_entry.grid(row =3, column=1)

#date label and entry field
today= date.today()
print(today)
date_label = CTkLabel(user_info_frame, text="Date")
date_label.grid(row=2, column=2, padx=5, pady=5)
date_lable = CTkLabel(user_info_frame, text=today)
date_entry = DateEntry(user_info_frame, date_pattern='dd/mm/yyyy', mindate=today, state="readonly")
date_lable.grid(row=3, column=2, padx=5, pady=5)

###########the title of the 3rd label frame 
engine_info_frame = CTkFrame(main_frame, fg_color="#006494", border_color="#3a7ca5", border_width=2)
engine_info_frame.grid(row = 2, column = 0, sticky="news", padx=5, pady=10)

##########Engine type label and entry field
ac_engine_label = CTkLabel(engine_info_frame, text="Engine Type")
ac_engine_label.grid(row=0, column=0)
ac_engine_combobox = CTkComboBox(engine_info_frame, values=["CFM", "PW1100G", "CFM"], state="readonly")
ac_engine_combobox.grid(row=1, column=0, padx = 5, pady=5)

########## Create two check buttons, link them to the IntVar, and set their values

checkbutton1 = tkinter.Radiobutton(engine_info_frame, text="KILO", variable=ki_lo_var, value=1, background="#3a7ca5" )
checkbutton1.grid(row=0, column=1, pady=5)
checkbutton2 = tkinter.Radiobutton(engine_info_frame, text="LIVRE", variable=ki_lo_var, value=2, background="#3a7ca5")
checkbutton2.grid(row=0, column=2, pady=5)



entry_manager = classes.EntryManager(ac_msn_entry, ac_version_entry, ac_fqi_part_entry, ac_fqi_serial_entry, ac_stamp_entry, date_entry, ac_engine_combobox, ki_lo_var)
frame_manager.created_frames.append(main_frame)
def on_start():
    if entry_manager.are_entries_filled():
        dictionary_page0 = entry_manager.handle_store_entries()
        with open('dictionary_page0.pkl', 'wb') as file:
            pickle.dump(dictionary_page0, file)
        create_new_frame(frame, next_page_button, start_button)
        configure_text_kilo_or_livre(ki_lo_var)
        error_label.config(text="", background="#003554")  # Clear any previous error message
    else:
        error_label.configure(text="Error: Please fill in all the entries.", fg="red", background="white")
        tkinter.messagebox.showerror("Error", "Please fill in all the entries.")
###########the title of the 4th label frame 
start_reset_frame = CTkFrame(main_frame, fg_color="#003554")
start_reset_frame.grid(row = 3, column = 0, sticky="news", padx=5, pady=5)

start_button = CTkButton(start_reset_frame, fg_color="#051923", text="Start", command = on_start)
start_button.grid(row=0, column=0, padx=5)

error_label = tkinter.Label(main_frame, text="",  background="#003554")
error_label.grid(row=4, column=0, pady=(0, 10))


def on_reset(): 
    entry_manager.reset_entries()
    erase_page1_entries()
    erase_page2_entries()
    destroy_second_frame(frame)
    next_page_button.configure(state=tkinter.DISABLED)
    start_button.configure(state=tkinter.NORMAL)
def on_next_page_button():
    if entry_manager.are_entries_filled():
        entry_manager.handle_store_entries()
        dictionary_page0 = entry_manager.handle_store_entries()
        with open('dictionary_page0.pkl', 'wb') as file:
            pickle.dump(dictionary_page0, file)
        configure_text_kilo_or_livre(ki_lo_var)
        go_to_next_page()
        error_label.configure(text="", background="#003554")  # Clear any previous error message
    else:

        error_label.configure(text="Error: Please fill in all the entries.", background="white" )
        tkinter.messagebox.showerror("Error", "Please fill in all the entries.")


    
reset_button = CTkButton(start_reset_frame, text="Reset",fg_color="red", command= on_reset)
reset_button.grid(row=0, column=2, padx=5)

next_page_button = CTkButton(start_reset_frame, text="Next Page",fg_color="#051923", command=on_next_page_button)
next_page_button.grid(row=0, column=1, padx=15)
next_page_button.configure(state=tkinter.DISABLED)  # Initially disabled



window.mainloop()