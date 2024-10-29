#!/usr/bin/python3

"""
Script that prints the first State object from the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(username, password, 'localhost', database))

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
