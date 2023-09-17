#!/usr/bin/python3
""" Prints the first State object from the database """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password
