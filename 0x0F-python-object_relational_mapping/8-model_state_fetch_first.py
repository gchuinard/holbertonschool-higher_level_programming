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

    if len(argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).first()
    if query:
        print('{}: {}'.format(query.id, query.name))
    else:
        print("Nothing")
    session.close()
