#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa"""

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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
