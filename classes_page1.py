import tkinter

class page1_EntryManager:
    page1_entries = []

    def __init__(self, left_pump1_entry, left_pump2_entry, right_pump1_entry, right_pump2_entry, start_mass1_entry, end_mass1_entry, start_mass2_entry, end_mass2_entry, mass_rate1_result, mass_rate2_result):
        self.left_pump1_entry = left_pump1_entry
        self.left_pump2_entry = left_pump2_entry
        self.right_pump1_entry = right_pump1_entry
        self.right_pump2_entry = right_pump2_entry

        self.start_mass1_entry = start_mass1_entry
        self.end_mass1_entry = end_mass1_entry

        self.start_mass2_entry = start_mass2_entry
        self.end_mass2_entry = end_mass2_entry
        self.mass_rate1_result = mass_rate1_result
        self.mass_rate2_result = mass_rate2_result
        
        self.page1_entries = [left_pump1_entry, left_pump2_entry, right_pump1_entry, right_pump2_entry, start_mass1_entry, end_mass1_entry, start_mass2_entry, end_mass2_entry]
    
    def are_entries_filled(self):
        return all(entry.get() for entry in self.page1_entries)

    def check_mass_rates(self, mass_rate1_result, mass_rate2_result):
        mass_rate1_text = mass_rate1_result.cget("text")
        mass_rate2_text = mass_rate2_result.cget("text")
    
        return mass_rate1_text and mass_rate2_text and mass_rate1_text != "Invalid input" and mass_rate2_text != "Invalid input"

    
    def store_entries(self, check):
        left_pump1 = self.left_pump1_entry.get()
        left_pump2 = self.left_pump2_entry.get()
        right_pump1 = self.right_pump1_entry.get()
        right_pump2 = self.right_pump2_entry.get()

        start_mass1 = self.start_mass1_entry.get()
        end_mass1 = self.end_mass1_entry.get()
        start_mass2 = self.start_mass2_entry.get()
        end_mass2 = self.end_mass2_entry.get()
        mass_rate1_result_value = self.mass_rate1_result.cget("text")
        mass_rate2_result_value = self.mass_rate2_result.cget("text")
        if check == 1:
            entry_data_page1 = {
            "Left Pump 1 P(bar)": left_pump1, 
            "Left Pump 2 P(bar)": left_pump2, 
            "Right Pump 1 P(bar)": right_pump1, 
            "Right Pump 2 P(bar)": right_pump2, 
            "Jet Pump 1 start mass": start_mass1,
            "Jet Pump 1 end mass": end_mass1, 
            "Jet Pump 2 start mass": start_mass2,
            "Jet Pump 2 end mass": end_mass2,
            "Mass Rate 1 (kg/min)": mass_rate1_result_value,
            "Mass Rate 2 (kg/min)": mass_rate2_result_value
            }
        elif check == 2:
            entry_data_page1 = {
            "Left Pump 1 P(bar)": left_pump1, 
            "Left Pump 2 P(bar)": left_pump2, 
            "Right Pump 1 P(bar)": right_pump1, 
            "Right Pump 2 P(bar)": right_pump2, 
            "Jet Pump 1 start mass": start_mass1,
            "Jet Pump 1 end mass": end_mass1, 
            "Jet Pump 2 start mass": start_mass2,
            "Jet Pump 2 end mass": end_mass2,
            "Mass Rate 1 (lb/min)": mass_rate1_result_value,
            "Mass Rate 2 (lb/min)": mass_rate2_result_value
            }
        print(entry_data_page1)
        return entry_data_page1

    def reset_entries_page1(self):
        self.left_pump1_entry.delete(0, tkinter.END)
        self.left_pump2_entry.delete(0, tkinter.END)
        self.right_pump1_entry.delete(0, tkinter.END)
        self.right_pump2_entry.delete(0, tkinter.END)

        self.start_mass1_entry.delete(0, tkinter.END)
        self.end_mass1_entry.delete(0, tkinter.END)
        self.start_mass2_entry.delete(0, tkinter.END)
        self.end_mass2_entry.delete(0, tkinter.END)
        
        self.page1_entries.clear()
    
    
        
