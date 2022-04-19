from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from menkes import Ship, Captain, Klientas, Region, Fish
from tkinter import *

engine = create_engine('sqlite:///menkes_db.db')
Session = sessionmaker(bind=engine)
session = Session()

def right_listbox_fill(self):
    right_listbox.delete(0, END)
    laivo_metai = []
    sarasas = []
    left_selection = left_listbox.get(left_listbox.curselection())
    # vart_id = str(left_selection[1])
    laivo_metai = session.query(Ship).filter(Ship.name == left_selection).all()
    laivo_kapitonas = session.query(Captain).join(Ship).filter(Ship.name == left_selection).all()
    print(laivo_kapitonas)
    for i in laivo_metai:
        sarasas.append(f"Laivas pagamintas {i.prod_year} metais")
        sarasas.append(f"ir talpina {i.passanger_count} keleivių") 
    for i in laivo_kapitonas:
        sarasas.append(f"Laivo kapitonas {i.f_name} {i.l_name} plaukioja jau {i.experience} metus")
        
    
    keleiviu_kiekis = session.query(Ship.passanger_count).filter(Ship.name == left_selection).all()
    # sarasas = f"Laivo metai: {laivo_metai}"
       
    # print(sarasas)
    right_listbox.insert(0, *sarasas)
    # right_listbox.insert(1, *keleiviu_kiekis)

langas = Tk()
langas.geometry("400x200")
scrollbaras = Scrollbar(langas)
left_listbox = Listbox(langas, width=30, yscrollcommand = scrollbaras.set)
right_listbox = Listbox(langas, width=50, yscrollcommand = scrollbaras.set)
scrollbaras.config(command=left_listbox.yview)
rezultatas = Listbox(langas)
left_listbox.bind("<<ListboxSelect>>", right_listbox_fill)
but =Button(langas, text="Rodyti", command=right_listbox_fill)
left_listbox.grid(row=0, column=0)
right_listbox.grid(row=0, column=1)
but.grid(row=1, column=1)

def left_listbox_fill():
    left_listbox.delete(0, END)
    laivu_sarasas = session.query(Ship).all()
    laivu_vardu_sarasas = []
    for i in laivu_sarasas:    
        laivu_vardu_sarasas.append(i.name)
    left_listbox.insert(0, *laivu_vardu_sarasas)
left_listbox_fill()





langas.mainloop()