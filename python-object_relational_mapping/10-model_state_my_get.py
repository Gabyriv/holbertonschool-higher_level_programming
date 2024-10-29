#!/usr/bin/python3

"""
Script that print the State object with the name passed
as argument from the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(username, password, 'localhost', database))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).where(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
