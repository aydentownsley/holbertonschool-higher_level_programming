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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sesh = Session()

    states_a = sesh.query(State).filter(State.name.like('%a%'))

    for states in states_a:
        sesh.delete(states)
        sesh.commit()

    sesh.close()
