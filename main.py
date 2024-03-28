#!/usr/bin/env python3

from os import getenv
import models
from models.city import City
from models.base_model import Base, BaseModel
from models.base_model import Column, relationship, String
from models.state import State

type = getenv('HBNB_TYPE_STORAGE')
if __name__ == '__main__':
    # st1 = State(name="Alabama")
    # st2 = State(name="Arizona")
    # st3 = State(name="California")
    # st4 = State(name="Colorado")
    # st5 = State(name="Florida")
    # st6 = State(name="Georgia")
    # st7 = State(name="Hawaii")
    # st8 = State(name="Indiana")

    # ct1 = City(state_id = st1.id, name="Akron")
    # ct2 = City(state_id = st1.id, name="Douglas")
    # ct3 = City(state_id = st1.id, name="San Francisco")
    # ct4 = City(state_id = st2.id, name="Denver")
    # ct5 = City(state_id = st2.id, name="Miami")
    # ct6 = City(state_id = st2.id, name="nagrig")
    # ct7 = City(state_id = st3.id, name="Joliet")
    # ct8 = City(state_id = st3.id, name="Honolulu")
    # ct9 = City(state_id = st3.id, name="Chicago")
    # ct10 = City(state_id = st4.id, name="New Orleans")
    # ct11 = City(state_id = st4.id, name="san")
    # ct12 = City(state_id = st4.id, name="Saint Paul")
    # ct13 = City(state_id = st5.id, name="Jackson")
    # ct14 = City(state_id = st5.id, name="Portland")
    # ct15 = City(state_id = st5.id, name="Babbie")
    # ct16 = City(state_id = st6.id, name="Hanasham")
    # ct17 = City(state_id = st6.id, name="emadshama")
    # ct18 = City(state_id = st6.id, name="kolisedi")
    # ct19 = City(state_id = st7.id, name="alipapa")
    # ct20 = City(state_id = st7.id, name="honololo")
    # ct21 = City(state_id = st7.id, name="sedoali")
    # ct22 = City(state_id = st8.id, name="gappharkga")
    # ct23 = City(state_id = st8.id, name="telethwlwa")
    # ct24 = City(state_id = st8.id, name="hahhah")

    # models.storage.save_all([st1,st2, st3, st4, st5, st6, st7, st8,ct1,ct2,ct3,ct4,ct5,ct6,ct7,ct8,ct9,ct10,ct11,ct12,ct13,ct14,ct15,ct16,ct17,ct18,ct19,ct20,ct21,ct22,ct23,ct24])
   
    all_states = models.storage.all(State)
    for state_id, state in all_states.items():
        for city in state.cities:
            print("Find the city {} in the state {}".format(city.name, state))
