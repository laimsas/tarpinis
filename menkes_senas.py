from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///menkes_db.db')
Base = declarative_base()

class Ship(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("Pavadinimas", String)
    address = Column("Adresas", String)
    prod_year = Column("Gamybos metai", Integer) 
    passanger_count = Column("Keleivių skaičius", String)
    trip_price = Column("Kelionės kaina", Float)
    description = Column("Aprašymas", String)
    captains = relationship("Captain", back_populates = "ship")

    def __repr__(self):  
        return f"{self.name} {self.address} {self.prod_year} {self.passanger_count} {self.trip_price} {self.description}"

class Captain(Base):
    __tablename__ = 'captains'
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String)
    l_name = Column(String)
    experience = Column(Integer)
    description = Column(String)
    ship_id = Column(Integer, ForeignKey('ships.id'))
    ship = relationship("Ship", back_populates = "captains")



    def __repr__(self):  
        return f"{self.f_name} {self.l_name} {self.experience} {self.description}"

class Klientas(Base):
    __tablename__ = 'klientai'
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String)
    l_name = Column(String)
    tel_no = Column(Integer)
    e_mail = Column(String)
    # saskaitos = relationship("Saskaita", back_populates = 'klientas')

    def __repr__(self):  
        return f"{self.f_name} {self.l_name} {self.tel_no} {self.e_mail}"

class Region(Base):
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    baltic_sea = Column('Baltijos jūra', Integer)
    curonian_lagoon = Column('Kuršių marios', Integer)
    nemunas = Column('Nemunas', Integer)
    ship_id = Column(Integer, ForeignKey('ships.id'))

    def __repr__(self):  
        return f"{self.baltic_sea} {self.curonian_lagoon} {self.nemunas}"

class Fish(Base):
    __tablename__ = 'fishes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cod = Column('Menkės', Integer)
    salomon = Column('Lašišos', Integer)
    sea_trout = Column('Šlakiai', Integer)
    zander = Column('Starkiai', Integer)
    smelt = Column('Stintos', Integer)
    white_fish = Column('Balta žuvis', Integer)
    ship_id = Column(Integer, ForeignKey('ships.id'))


Base.metadata.create_all(engine)