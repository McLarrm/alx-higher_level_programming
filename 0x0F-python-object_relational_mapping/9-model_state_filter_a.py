#!/usr/bin/python3
""" Lists all State objects that contain the letter 'a' from the database """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

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

    results = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in results:
        print("{}: {}".format(state.id, state.name))

    session.close()
