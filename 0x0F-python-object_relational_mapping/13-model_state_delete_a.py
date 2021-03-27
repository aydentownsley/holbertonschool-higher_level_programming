#!/usr/bin/python3
""" adds Louisiana state object to table """

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uname = sys.argv[1]
    pword = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           uname, pword, dbase))
    Session = sessionmaker(bind=engine)
    sesh = Session()

    for states in sesh.query(State).order_by(State.id):
        if 'a' in states.name:
            sesh.delete(states)

    sesh.commit()
    sesh.close()
