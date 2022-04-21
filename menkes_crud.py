from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from menkes import Ship, Captain, Klientas, Region, Fish
from tkinter import *
from tkinter import ttk

engine = create_engine('sqlite:///menkes_db.db')
Session = sessionmaker(bind=engine)
session = Session()

# def regions_list():
#     global regionai_list
#     regionai_list = []
#     regionai = session.query(Region).group_by(Region.region_name).all()
#     for i in regionai:
#         print(i.region_name)
#         regionai_list.append(i.region_name)
#     # print(regionai_list)
#     return regionai_list
# regions_list()

def right_listbox_fill(self):
    right_listbox.delete(0, END)
    laivo_metai = []
    sarasas = []
    left_selection = left_listbox.get(left_listbox.curselection())
    # vart_id = str(left_selection[1])
    laivo_metai = session.query(Ship).filter(Ship.name == left_selection).all()
    laivo_kapitonas = session.query(Captain).join(Ship).filter(Ship.name == left_selection).all()
    # print(laivo_kapitonas)
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
label_fish = Label(langas, text = "Pagal žuvį")
label_fish.grid(column=0, row=0)
label_region = Label(langas, text= "Pagal vietą")
label_region.grid(column=1, row= 0)
scrollbaras = Scrollbar(langas)
combo_fish = ttk.Combobox(langas, 
                            values=[
                                    "------",
                                    "Menkė", 
                                    "Lašiša",
                                    "Šlakis",
                                    "Starkis",
                                    "Stinta",
                                    "Balta žuvis"])
combo_fish.grid(column=0, row=1)
combo_fish.current(0)
combo_region = ttk.Combobox(langas, 
                            values=[
                                    "------",
                                    "Baltijos jūra", 
                                    "Kuršių marios",
                                    "Nemunas"])
combo_region.grid(column=1, row= 1)
combo_region.current(0)
left_listbox = Listbox(langas, width=30, yscrollcommand = scrollbaras.set)
right_listbox = Listbox(langas, width=50, yscrollcommand = scrollbaras.set)
scrollbaras.config(command=left_listbox.yview)
rezultatas = Listbox(langas)
left_listbox.bind("<<ListboxSelect>>", right_listbox_fill)

def left_listbox_update(event):
    left_listbox.delete(0, END)
    combo_fish_result = combo_fish.get()
    print('Pasiimam dropboxo reiksme: ', combo_fish_result)
    zuvis = session.query(Fish).filter(Fish.fish_name == combo_fish_result).first()
    # print(zuvu_sarasas)
        # print(i.fish_name)
    if zuvis.fish_name == combo_fish_result:
        # print(f'radom atitikmeni {zuvis.fish_name}')
        tinkami_laivai = session.query(Ship).join(Fish).filter(Fish.fish_name == zuvis.fish_name).all()
        laivu_vardu_sarasas = []
        for i in tinkami_laivai:    
            print(i.name)
            laivu_vardu_sarasas.append(i.name)
        left_listbox.insert(0, *laivu_vardu_sarasas)

combo_fish.bind("<<ComboboxSelected>>", left_listbox_update)
# but =Button(langas, text="Rodyti", command=left_listbox_update)
left_listbox.grid(row=3, column=0)
right_listbox.grid(row=3, column=1)
# but.grid(row=1, column=1)

def left_listbox_fill():
    left_listbox.delete(0, END)
    laivu_sarasas = session.query(Ship).all()
    laivu_vardu_sarasas = []
    for i in laivu_sarasas:    
        laivu_vardu_sarasas.append(i.name)
    left_listbox.insert(0, *laivu_vardu_sarasas)
left_listbox_fill()






langas.mainloop()