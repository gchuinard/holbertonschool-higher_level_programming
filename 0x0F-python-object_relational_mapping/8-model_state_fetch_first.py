#!/usr/bin/python3
'''
prints the first State object from the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': user, 'password': password, 'database': db_name}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    try:
        instance = session.query(State).order_by(State.id).limit(1).all()[0]
        print("{}: {}".format(instance.id, instance.name))
    except:
        print("Nothing")