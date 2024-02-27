import tkinter

class page2_EntryManager:
    page2_entries = []

    def __init__(self, Fuel_Density_entry, Fuel_Temperature_entry, Ambient_Temperature_entry, Pitch_entry, Roll_entry,
                 stp1_volume_entry, stp1_FOB_entry, step1_uplifted, stp1_left_entry, stp1_center_entry, stp1_right_entry,
                 stp2_volume_entry, stp2_FOB_entry, step2_uplifted, stp2_left_entry, stp2_center_entry, stp2_right_entry,
                 stp3_volume_entry, stp3_FOB_entry, step3_uplifted, stp3_left_entry, stp3_center_entry, stp3_right_entry):
        self.Fuel_Density_entry = Fuel_Density_entry
        self.Fuel_Temperature_entry = Fuel_Temperature_entry
        self.Ambient_Temperature_entry = Ambient_Temperature_entry
        self.Pitch_entry = Pitch_entry

        self.Roll_entry = Roll_entry
        self.stp1_volume_entry = stp1_volume_entry
        self.stp1_FOB_entry = stp1_FOB_entry
        self.step1_uplifted = step1_uplifted
        self.stp1_left_entry = stp1_left_entry
        self.stp1_center_entry = stp1_center_entry
        self.stp1_right_entry = stp1_right_entry
        
        self.stp2_volume_entry = stp2_volume_entry
        self.stp2_FOB_entry = stp2_FOB_entry
        self.step2_uplifted = step2_uplifted
        self.stp2_left_entry = stp2_left_entry
        self.stp2_center_entry = stp2_center_entry
        self.stp2_right_entry = stp2_right_entry
        
        self.stp3_volume_entry = stp3_volume_entry
        self.stp3_FOB_entry = stp3_FOB_entry
        self.step3_uplifted = step3_uplifted
        self.stp3_left_entry = stp3_left_entry
        self.stp3_center_entry = stp3_center_entry
        self.stp3_right_entry = stp3_right_entry
        
        self.page1_entries = [Fuel_Density_entry, Fuel_Temperature_entry, Ambient_Temperature_entry, Pitch_entry, Roll_entry,
                 stp1_volume_entry, stp1_FOB_entry, stp1_left_entry, stp1_right_entry,
                 stp2_volume_entry, stp2_FOB_entry, stp2_left_entry, stp2_center_entry, stp2_right_entry,
                 stp3_volume_entry, stp3_FOB_entry, stp3_left_entry, stp3_center_entry, stp3_right_entry]
    
    def are_entries_filled(self):
        return all(entry.get() for entry in self.page1_entries)
    
    def store_entries(self):
        Fuel_Density = self.Fuel_Density_entry.get() 
        Fuel_Temperature = self.Fuel_Temperature_entry.get()
        Ambient_Temperature = self.Ambient_Temperature_entry.get()
        Pitch = self.Pitch_entry.get()

        Roll = self.Roll_entry.get()
        stp1_volume = self.stp1_volume_entry.get()
        stp1_FOB = self.stp1_FOB_entry.get()
        stp1_uplifted = self.step1_uplifted
        stp1_left = self.stp1_left_entry.get()
        #stp1_center = self.stp1_center_entry.get()
        stp1_right = self.stp1_right_entry.get()
        
        stp2_volume = self.stp2_volume_entry.get()
        stp2_FOB = self.stp2_FOB_entry.get()
        stp2_uplifted = self.step2_uplifted
        stp2_left = self.stp2_left_entry.get()
        stp2_center = self.stp2_center_entry.get()
        stp2_right = self.stp2_right_entry.get()
        
        stp3_volume = self.stp3_volume_entry.get()
        stp3_FOB = self.stp3_FOB_entry.get()
        stp3_uplifted = self.step3_uplifted
        stp3_left = self.stp3_left_entry.get()
        stp3_center = self.stp3_center_entry.get()
        stp3_right = self.stp3_right_entry.get()

        entry_data_page2 = {
        "Fuel_Density" : Fuel_Density,
        "Fuel_Temperature" : Fuel_Temperature,
        "Ambient_Temperature" : Ambient_Temperature,
        "Pitch" : Pitch,
        "Roll" : Roll,
        "stp1 volume" : stp1_volume,
        "step1 FOB" : stp1_FOB,
        "step1 uplifted": stp1_uplifted,
        "step1 left" : stp1_left,
        #"step1 center" : stp1_center,
        "step1 right" : stp1_right,
        "stp2 volume" : stp2_volume,
        "step2 FOB" : stp2_FOB,
        "step2 uplifted": stp2_uplifted,
        "step2 left" : stp2_left,
        "step2 center" : stp2_center,
        "step2 right" : stp2_right,
        "stp3 volume" : stp3_volume,
        "step3 FOB" : stp3_FOB,
        "step3 uplifted": stp3_uplifted,
        "step3 left" : stp3_left,
        "step3 center" : stp3_center,
        "step3 right" : stp3_right
        }
        print(entry_data_page2)
        return entry_data_page2

    def reset_entries_page2(self):

        self.Fuel_Density_entry.delete(0, tkinter.END)
        self.Fuel_Temperature_entry.delete(0, tkinter.END)
        self.Ambient_Temperature_entry.delete(0, tkinter.END)
        self.Pitch_entry.delete(0, tkinter.END)

        self.Roll_entry.delete(0, tkinter.END)
        self.stp1_volume_entry.delete(0, tkinter.END)
        self.stp1_FOB_entry.delete(0, tkinter.END)
        #self.step1_uplifted.delete(0, tkinter.END)
        self.stp1_left_entry.delete(0, tkinter.END)
        #stp1_center = self.stp1_center_entry.get()
        self.stp1_right_entry.delete(0, tkinter.END)
        
        self.stp2_volume_entry.delete(0, tkinter.END)
        #self.step2_uplifted.delete(0, tkinter.END)
        self.stp2_FOB_entry.delete(0, tkinter.END)
        self.stp2_left_entry.delete(0, tkinter.END)
        self.stp2_center_entry.delete(0, tkinter.END)
        self.stp2_right_entry.delete(0, tkinter.END)
        
        self.stp3_volume_entry.delete(0, tkinter.END)
        self.stp3_FOB_entry.delete(0, tkinter.END)
        #self.step3_uplifted.delete(0, tkinter.END)
        self.stp3_left_entry.delete(0, tkinter.END)
        self.stp3_center_entry.delete(0, tkinter.END)
        self.stp3_right_entry.delete(0, tkinter.END)
        
        self.page2_entries.clear()
