#!/usr/bin/python3

"""
Script that prints all City objects
from the database.
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = ''
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(username, password, 'localhost', database))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
