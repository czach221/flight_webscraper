import tkinter as tk
from tkinter import ttk
import datetime
from tkcalendar import Calendar
#import webscraper as ws

class FlightSearchApp:
    def __init__(self, master):
        self.master = master
        master.title("Cheapest Flights Search")
        master.geometry("1000x200")  # Set window size to 800x600

        # Styling
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12), background="#4f72ff", foreground="white")
        style.configure("TEntry", font=("Helvetica", 12), background="white")
        style.configure("TCombobox", font=("Helvetica", 12))
        style.configure("Enhanced.TCombobox", font=("Helvetica", 12), fieldbackground="lightblue", background="lightblue", arrowcolor="blue")


        self.label = ttk.Label(master, text="Cheapest Flights", font=("Helvetica", 24, "bold"))
        self.label.grid(row=0, column=2)

        # Departure Location Combobox
        self.departure_label = ttk.Label(master, text="Departure Location:")
        self.departure_label.grid(row=1, column=0)
        self.departure_entry = ttk.Combobox(master, width=20)
        self.departure_entry.grid(row=2, column=0)
        self.departure_entry['values'] = ["Select an airport"]  # Add airport list here
        self.departure_entry = ttk.Combobox(master, width=50, style="Enhanced.TCombobox")
        

        # Arrival Location Combobox
        self.arrival_label = ttk.Label(master, text="Arrival Location:")
        self.arrival_label.grid(row=1, column=1)
        self.arrival_entry = ttk.Combobox(master, width=20)
        self.arrival_entry.grid(row=2, column=1)
        self.arrival_entry['values'] = ["Select an airport"]  # Add airport list here
        self.arrival_entry = ttk.Combobox(master, width=50, style="Enhanced.TCombobox")

        # Departure Date Entry
        self.departure_date_label = ttk.Label(master, text="Departure Date:")
        self.departure_date_label.grid(row=1, column=3)

        self.departure_date_entry = ttk.Entry(master, width=20)
        self.departure_date_entry.grid(row=2, column=3, padx=10, pady=10)
        #self.departure_date_entry.bind("<Button-1>", lambda event: self.open_and_select_date(event, 'departure'))

        # Return Date Entry
        self.return_date_label = ttk.Label(master, text="Return Date:")
        self.return_date_label. grid(row=1, column=4)

        self.return_date_entry = ttk.Entry(master, width=20)
        self.return_date_entry.grid(row=2, column=4, padx=10, pady=10)
        #self.return_date_entry.bind("<Button-1>", lambda event: self.open_and_select_date(event))


        # Search Button
        self.search_button = ttk.Button(master, text="Search Flights", command=self.search_flights)
        self.search_button.grid(row=4, column=2)


        #Webscraper Aufruf
        departure_airport= self.departure_entry.get()
        arrival_airport = self.arrival_entry.get()
        deprture_date = self. departure_date_entry.get()
        return_date = self. return_date_entry.get()
        print(departure_airport, arrival_airport, deprture_date, return_date)
        #ws.webscraper_kayak(departure_airport, arrival_airport, )
        

    def search_flights(self):
        # Implement functionality to search flights based on user input
        departure_airport= self.departure_entry.get()
        arrival_airport = self.arrival_entry.get()
        deprture_date = self. departure_date_entry.get()
        return_date = self. return_date_entry.get()
        print(departure_airport, arrival_airport, deprture_date, return_date)

    def open_and_select_date(self, event, entry_name=''):
        top = tk.Toplevel(self.master)
        top.title("Wähle ein Datum")
        cal = Calendar(top, selectmode='day', year=2023, month=5, day=13)
        cal.pack(pady=20, padx=20)

        if entry_name == 'departure': 
            select_button = ttk.Button(top, text="Datum wählen", command=lambda: self.set_departure_date(cal, top))
            select_button.pack()
        else: 
            select_button = ttk.Button(top, text="Datum wählen", command=lambda: self.set_return_date(cal, top))
            select_button.pack()
    
    def set_departure_date(self, cal, top):
        date = cal.get_date()
        self.departure_date_entry.delete(0, tk.END)
        self.departure_date_entry.insert(0, date)
        top.destroy()

    def set_return_date(self, cal, top):
        date = cal.get_date()
        self.return_date_entry.delete(0, tk.END)
        self.return_date_entry.insert(0, date)
        top.destroy()

def main():
    root = tk.Tk()
    app = FlightSearchApp(root)
    root.mainloop()


main()


