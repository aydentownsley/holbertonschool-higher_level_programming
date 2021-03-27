#!/usr/bin/python3
""" Print first satte from htbn6 """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uname = sys.argv[1]
    pword = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            uname, pword, dbname))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sesh = Session()

    fstate = sesh.query(State).first()
    if fstate:
        print("{}: {}".format(fstate.id, fstate.name))
    else:
        print("Nothing")

    sesh.close()
