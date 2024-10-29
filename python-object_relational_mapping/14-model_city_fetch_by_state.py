#!/usr/bin/python3
"""Script to list all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    connection_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection_str.format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(State.id == City.state_id)\
                   .order_by(City.id)

    for state, city in query.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
