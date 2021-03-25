#!/usr/bin/python3
'''
lists all State objects form database hbtn_0e_0_usa
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    for state in sesh.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    sesh.close
