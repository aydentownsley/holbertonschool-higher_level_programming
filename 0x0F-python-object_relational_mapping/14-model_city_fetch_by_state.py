#!/usr/bin/python3
""" adds Louisiana state object to table """

import sys
from model_state import State, Base
from model_city import City
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

    for row in sesh.query(City, State).join(
               State, City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(row[1].name, row[0].id, row[0].name))

    sesh.close()
