import tkinter as tk
from tkcalendar import  Calendar, DateEntry
ventana=tk.Tk()
ventana.title("Calendario")
data_entry=DateEntry(ventana, date_pattern='dd-mm-yy' )
data_entry.bind('<<DateEntrySelected>>', lambda e: print(data_entry.get()))

data_entry.pack()
"""
def print_date(date):
    print(date)

cal=Calendar(ventana, selectmode='day',locale='es_ES',date_pattern='y-mm-dd')

cal.pack()
cal.bind("<<CalendarSelected>>", lambda e: print_date(cal.get_date()))
"""


ventana.mainloop()