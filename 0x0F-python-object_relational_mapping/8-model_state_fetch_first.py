#!/usr/bin/python3
'''
prints the first State object from the database hbtn_0e_6_usa
'''

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        states = session.query(State).first()
        print("{}: {}".format(states.id, states.name))
    except:
        print("Nothing")
    session.commit()
    session.close()