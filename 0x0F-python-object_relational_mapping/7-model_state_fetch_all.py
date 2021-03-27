#!/usr/bin/python3
""" All states form tabel """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    for state in sesh.query(State).order_by(State.id.asc()):
        print("{}: {}".format(state.id, state.name))
    sesh.close()
