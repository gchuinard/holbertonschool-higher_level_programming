#!/usr/bin/python3
'''
prints the first State object from the database hbtn_0e_6_usa
'''

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

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
