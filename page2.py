#!/usr/bin/python3
import tkinter
import classes_page2
import pickle
from write import main
from write_excel_correct_file import main_excel

checker_page2 = None
def configure_text_kilo_or_livre_page2(check):
        global checker_page2
        checker_page2 = check
        print(checker_page2)
        if checker_page2 == 2:
             uplifted_fuel_parameters_frame.config(text = "Uplifted Fuel Parameters - lb")
        else:
            pass
def go_to_second_page():
    second_frame.grid(row=0, column=0, sticky="news")
    
def destroy_second_frame(frame2tobedestroyed):
    # Destroy the new frame
        frame2tobedestroyed.grid_forget()
def erase_page2_entries():
        page2_entry_manager.reset_entries_page2()
def create_2nd_frame(frame, button, continue_button):
    next_page_button = button
    next_page_button.configure(state=tkinter.NORMAL)
    continue_button.configure(state=tkinter.DISABLED)
    # Create a new frame
    global second_frame
    global uplifted_fuel_parameters_frame
    second_frame = tkinter.Frame(frame)
    second_frame.grid(row=0, column=0, sticky="news")
    #next_page_button.configure(command=lambda: go_to_second_page(second_frame))
    
    fuel_quantity_indicator_frame = tkinter.LabelFrame(second_frame, text = "Fuel Quantity Indicator Accuracy")
    fuel_quantity_indicator_frame.grid(row = 2, column = 0, sticky="news", padx=20, pady=10)

    desnsity_temperature_frame = tkinter.LabelFrame(fuel_quantity_indicator_frame, text = "Fuel Density and Temperature")
    desnsity_temperature_frame.grid(row = 0, column = 0, sticky="news", padx=20, pady=10)

    Fuel_Density_label = tkinter.Label(desnsity_temperature_frame, text="Fuel Density")
    Fuel_Density_label.grid(row=0, column=0)
    Fuel_Density_entry = tkinter.Entry(desnsity_temperature_frame)
    Fuel_Density_entry.grid(row=0, column=1)

    Fuel_Temperature_label = tkinter.Label(desnsity_temperature_frame, text="Fuel Temperature")
    Fuel_Temperature_label.grid(row=0, column=2)
    Fuel_Temperature_entry = tkinter.Entry(desnsity_temperature_frame)
    Fuel_Temperature_entry.grid(row=0, column=3)

    Ambient_Temperature_label = tkinter.Label(desnsity_temperature_frame, text="Ambient Temperature")
    Ambient_Temperature_label.grid(row=0, column=4)
    Ambient_Temperature_entry = tkinter.Entry(desnsity_temperature_frame)
    Ambient_Temperature_entry.grid(row=0, column=5)

    #####################################################################

    pitch_and_roll_frame = tkinter.LabelFrame(fuel_quantity_indicator_frame, text = "Air Craft Orientation ")
    pitch_and_roll_frame.grid(row = 1, column = 0, sticky="news", padx=20, pady=10)

    Pitch_label = tkinter.Label(pitch_and_roll_frame, text="Pitch")
    Pitch_label.grid(row=0, column=0)
    Pitch_entry = tkinter.Entry(pitch_and_roll_frame)
    Pitch_entry.grid(row=0, column=1)

    Roll_label = tkinter.Label(pitch_and_roll_frame, text="Roll")
    Roll_label.grid(row=0, column=2)
    Roll_entry = tkinter.Entry(pitch_and_roll_frame)
    Roll_entry.grid(row=0, column=3)

    #####################################################################

    uplifted_fuel_parameters_frame = tkinter.LabelFrame(fuel_quantity_indicator_frame, text = "Uplifted Fuel Parameters - Kg")
    uplifted_fuel_parameters_frame.grid(row = 2, column = 0, sticky="news", padx=20, pady=10)

    step1_frame = tkinter.LabelFrame(uplifted_fuel_parameters_frame, text = "Step1")
    step1_frame.grid(row = 0, column = 0, sticky="news", padx=20, pady=10)
    stp1_volume_label = tkinter.Label(step1_frame, text="volume")
    stp1_volume_label.grid(row=0, column=0)
    stp1_volume_entry = tkinter.Entry(step1_frame)
    stp1_volume_entry.grid(row=0, column=1)


    stp1_FOB_label = tkinter.Label(step1_frame, text="FOB")
    stp1_FOB_label.grid(row=1, column=0)
    stp1_FOB_entry = tkinter.Entry(step1_frame)
    stp1_FOB_entry.grid(row=1, column=1)

    indicator_step1_frame = tkinter.LabelFrame(uplifted_fuel_parameters_frame, text = "step 1-Indicator")
    indicator_step1_frame.grid(row = 0, column = 1, sticky="news", padx=20, pady=10)
    
    stp1_left_label = tkinter.Label(indicator_step1_frame, text="LFT")
    stp1_left_label.grid(row=0, column=0)
    stp1_left_entry = tkinter.Entry(indicator_step1_frame)
    stp1_left_entry.grid(row=1, column=0)

    zero = 0
    stp1_center_label = tkinter.Label(indicator_step1_frame, text="CTR")
    stp1_center_label.grid(row=0, column=1)
    stp1_center_entry = tkinter.Label(indicator_step1_frame, borderwidth=1, relief="solid", width=17, height=1)
    stp1_center_entry.configure(text=f'{zero}')
    stp1_center_entry.grid(row=1, column=1)

    stp1_right_label = tkinter.Label(indicator_step1_frame, text="RT")
    stp1_right_label.grid(row=0, column=2)
    stp1_right_entry = tkinter.Entry(indicator_step1_frame)
    stp1_right_entry.grid(row=1, column=2)

    
    #####################################################
    step2_frame = tkinter.LabelFrame(uplifted_fuel_parameters_frame, text = "Step2")
    step2_frame.grid(row = 1, column = 0, sticky="news", padx=20, pady=10)
    stp2_volume_label = tkinter.Label(step2_frame, text="volume")
    stp2_volume_label.grid(row=0, column=0)
    stp2_volume_entry = tkinter.Entry(step2_frame)
    stp2_volume_entry.grid(row=0, column=1)

    stp2_FOB_label = tkinter.Label(step2_frame, text="FOB")
    stp2_FOB_label.grid(row=1, column=0)
    stp2_FOB_entry = tkinter.Entry(step2_frame)
    stp2_FOB_entry.grid(row=1, column=1)

    indicator_step2_frame = tkinter.LabelFrame(uplifted_fuel_parameters_frame, text = "step 2-Indicator")
    indicator_step2_frame.grid(row = 1, column = 1, sticky="news", padx=20, pady=10)
    
    stp2_left_label = tkinter.Label(indicator_step2_frame, text="LFT")
    stp2_left_label.grid(row=0, column=0)
    stp2_left_entry = tkinter.Entry(indicator_step2_frame)
    stp2_left_entry.grid(row=1, column=0)

    
    stp2_center_label = tkinter.Label(indicator_step2_frame, text="CTR")
    stp2_center_label.grid(row=0, column=1)
    stp2_center_entry = tkinter.Entry(indicator_step2_frame)
    stp2_center_entry.grid(row=1, column=1)

    stp2_right_label = tkinter.Label(indicator_step2_frame, text="RT")
    stp2_right_label.grid(row=0, column=2)
    stp2_right_entry = tkinter.Entry(indicator_step2_frame)
    stp2_right_entry.grid(row=1, column=2)

    
    ######################################################
    step3_frame = tkinter.LabelFrame(uplifted_fuel_parameters_frame, text = "Step3")
    step3_frame.grid(row = 2, column = 0, sticky="news", padx=20, pady=10)
    stp3_volume_label = tkinter.Label(step3_frame, text="volume")
    stp3_volume_label.grid(row=0, column=0)
    stp3_volume_entry = tkinter.Entry(step3_frame)
    stp3_volume_entry.grid(row=0, column=1)

    stp3_FOB_label = tkinter.Label(step3_frame, text="FOB")
    stp3_FOB_label.grid(row=1, column=0)
    stp3_FOB_entry = tkinter.Entry(step3_frame)
    stp3_FOB_entry.grid(row=1, column=1)

    indicator_step3_frame = tkinter.LabelFrame(uplifted_fuel_parameters_frame, text = "step 3-Indicator")
    indicator_step3_frame.grid(row = 2, column = 1, sticky="news", padx=20, pady=10)
    
    stp3_left_label = tkinter.Label(indicator_step3_frame, text="LFT")
    stp3_left_label.grid(row=0, column=0)
    stp3_left_entry = tkinter.Entry(indicator_step3_frame)
    stp3_left_entry.grid(row=1, column=0)

    
    stp3_center_label = tkinter.Label(indicator_step3_frame, text="CTR")
    stp3_center_label.grid(row=0, column=1)
    stp3_center_entry = tkinter.Entry(indicator_step3_frame)
    stp3_center_entry.grid(row=1, column=1)

    stp3_right_label = tkinter.Label(indicator_step3_frame, text="RT")
    stp3_right_label.grid(row=0, column=2)
    stp3_right_entry = tkinter.Entry(indicator_step3_frame)
    stp3_right_entry.grid(row=1, column=2)
    
    accuracy_frame = tkinter.LabelFrame(fuel_quantity_indicator_frame, text = "FQI Accuracy %")
    accuracy_frame.grid(row = 3, column = 0, sticky="w", padx=20, pady=10)
    Accuracy_label = tkinter.Label(accuracy_frame,borderwidth=1, relief="solid", width=17, height=1)
    Accuracy_label.grid(row=0, column=0, padx=20, pady=20)
    

    back_close_frame = tkinter.Frame(second_frame)
    back_close_frame.grid(row = 6, column = 0, sticky="news", padx=20, pady=20)
    #Back Button    
    back_button = tkinter.Button(back_close_frame, text="Back", command=lambda: destroy_second_frame(second_frame))
    back_button.grid(row=6, column=0, pady=(10, 0))

    error_label = tkinter.Label(second_frame, text="", fg="red")
    error_label.grid(row=7, column=0, pady=(0, 10))

    
    def on_run(): 
        if checker_page2 == 1:
            step1_uplifted = int(float(stp1_volume_entry.get()) * (float(Fuel_Density_entry.get()) + (float(Ambient_Temperature_entry.get()) - float(Fuel_Temperature_entry.get()))*0.0008))
            step2_uplifted = int(float(stp2_volume_entry.get()) * (float(Fuel_Density_entry.get()) + (float(Ambient_Temperature_entry.get()) - float(Fuel_Temperature_entry.get()))*0.0008))
            step3_uplifted = int(float(stp3_volume_entry.get()) * (float(Fuel_Density_entry.get()) + (float(Ambient_Temperature_entry.get()) - float(Fuel_Temperature_entry.get()))*0.0008))
        elif checker_page2 == 2:
            step1_uplifted = int(float(stp1_volume_entry.get()) * (float(Fuel_Density_entry.get()) + (float(Ambient_Temperature_entry.get()) - float(Fuel_Temperature_entry.get()))*0.0008) / 0.45359)
            step2_uplifted = int(float(stp2_volume_entry.get()) * (float(Fuel_Density_entry.get()) + (float(Ambient_Temperature_entry.get()) - float(Fuel_Temperature_entry.get()))*0.0008) / 0.45359)
            step3_uplifted = int(float(stp3_volume_entry.get()) * (float(Fuel_Density_entry.get()) + (float(Ambient_Temperature_entry.get()) - float(Fuel_Temperature_entry.get()))*0.0008) / 0.45359)
        
        FOB_difference = float(stp3_FOB_entry.get()) - float(stp2_FOB_entry.get())
        uplifted_difference = step3_uplifted - step2_uplifted
        accuracy = (FOB_difference / uplifted_difference) * 100 - 100
        Accuracy_label.configure(text=f'{accuracy:.2f}')
        global page2_entry_manager
        page2_entry_manager = classes_page2.page2_EntryManager(Fuel_Density_entry, Fuel_Temperature_entry, Ambient_Temperature_entry, Pitch_entry, Roll_entry,
                 stp1_volume_entry, stp1_FOB_entry, step1_uplifted, stp1_left_entry, stp1_center_entry, stp1_right_entry,
                 stp2_volume_entry, stp2_FOB_entry, step2_uplifted, stp2_left_entry, stp2_center_entry, stp2_right_entry,
                 stp3_volume_entry, stp3_FOB_entry, step3_uplifted, stp3_left_entry, stp3_center_entry, stp3_right_entry)
        
        if page2_entry_manager.are_entries_filled():
            dictionary_page2 = page2_entry_manager.store_entries()
            with open('dictionary_page0.pkl', 'rb') as file:
                dictionary_page0 = pickle.load(file)

            # Merge dictionaries
            new_key = 'Accuracy %'
            new_value = "{:.2f}".format(accuracy)
            dictionary_page0.update(dictionary_page2)
            dictionary_page0.update({new_key: new_value})
            with open('dictionary_page0.pkl', 'wb') as file:
                pickle.dump(dictionary_page0, file)
            main(checker_page2)
            main_excel()
            print(step1_uplifted)
            print(step2_uplifted)
            print(step3_uplifted)
            print(f'{accuracy:.2f}%')
            #go_to_second_page()
            error_label.config(text="")  # Clear any previous error message
        # hide_page1_frames()
        # entry_manager.reset_entries()
        else:
            error_label.config(text="Error: Please fill in all the entries.")
            tkinter.messagebox.showerror("Error", "Please fill in all the entries.")

    run_button = tkinter.Button(back_close_frame, text="run", command=on_run)
    run_button.grid(row=6, column=1, pady=(10, 0))

    def destroy_second_frame(frame2tobedestroyed):
    
    # Destroy the new frame
        frame2tobedestroyed.grid_forget()