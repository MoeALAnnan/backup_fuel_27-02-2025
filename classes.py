import tkinter

class EntryManager:
    

    def __init__(self, ac_msn_entry, ac_version_entry, ac_fqi_part_entry, ac_fqi_serial_entry, ac_stamp_entry, date_entry, ac_engine_combobox, ki_lo_var):
        self.ac_msn_entry = ac_msn_entry
        self.ac_version_entry = ac_version_entry
        self.ac_fqi_part_entry = ac_fqi_part_entry
        self.ac_fqi_serial_entry = ac_fqi_serial_entry

        self.ac_stamp_entry = ac_stamp_entry
        self.date_entry = date_entry
        self.ac_engine_combobox = ac_engine_combobox
        self.ki_lo_var = ki_lo_var
        self.entries = [ac_msn_entry, ac_version_entry, ac_fqi_part_entry, ac_fqi_serial_entry, ac_stamp_entry, date_entry, ac_engine_combobox, ki_lo_var]
    
    def store_entries(self):
        msn = self.ac_msn_entry.get()
        version = self.ac_version_entry.get()
        Part_Number = self.ac_fqi_part_entry.get()
        Serial_number = self.ac_fqi_serial_entry.get()
        Stamp = self.ac_stamp_entry.get()
        Date = self.date_entry.get()
        engine_type = self.ac_engine_combobox.get()
        kilo_or_livre = self.ki_lo_var.get()

    
        entry_data = {
        "MSN": msn, 
        "VERSION": version, 
        "Part Number": Part_Number, 
        "Serial Number": Serial_number, 
        "Stamp": Stamp, 
        "Date": Date, 
        "Engine Type": engine_type, 
        "KILO/LIVRE": kilo_or_livre,
        "RATE": None
        }
        
        return entry_data

    def handle_store_entries(self):
        entry_data = self.store_entries()
        if entry_data["KILO/LIVRE"] == 1:
            kilo_or_livre = "KILOGRAMMES" 
            entry_data["KILO/LIVRE"] = kilo_or_livre
            entry_data["RATE"] = 88
        elif entry_data["KILO/LIVRE"] == 2:
            kilo_or_livre = "LIVRE"
            entry_data["KILO/LIVRE"] = kilo_or_livre
            entry_data["RATE"] = 194
        else:
            kilo_or_livre = ""
            entry_data["KILO/LIVRE"] = kilo_or_livre
        
        return(entry_data)


    def are_entries_filled(self):
        variable = all(entry.get() for entry in self.entries)
        print({variable})

        return all(entry.get() for entry in self.entries) and self.ki_lo_var.get() != 0

    def reset_entries(self):
        self.ac_msn_entry.delete(0, tkinter.END)
        self.ac_version_entry.delete(0, tkinter.END)
        self.ac_fqi_part_entry.delete(0, tkinter.END)
        self.ac_fqi_serial_entry.delete(0, tkinter.END)
        self.ac_stamp_entry.delete(0, tkinter.END)
        self.date_entry.delete(0, tkinter.END)
        #self.ac_engine_combobox.delete(0, tkinter.END)
        self.ki_lo_var.set(0)
        self.entries.clear()
