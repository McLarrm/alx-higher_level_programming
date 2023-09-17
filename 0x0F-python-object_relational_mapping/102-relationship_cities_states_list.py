#!/usr/bin/python3
"""List all City objects with associated State from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    Base.metadata.create_all(engine)

    session = Session(engine)

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = city.state.name
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    session.close()
