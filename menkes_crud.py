from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from menkes import Ship, Captain, Klientas, Region, Fish
from tkinter import *

engine = create_engine('sqlite:///menkes_db.db')
Session = sessionmaker(bind=engine)
session = Session()

def listas():
    lista = session.query(Captain.f_name, Captain.l_name, Ship.name).filter(Captain.ship_id == '2').all()
    print("Spausdinam")
    print(lista)
    

listas()