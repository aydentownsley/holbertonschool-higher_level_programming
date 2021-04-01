#!/usr/bin/python3
""" 100 main class """

import sqlalchemy
import sys
from relationship_city import Base, City
from relationship_state import Base, State
from sqlalchemy import create_engine
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

    for row in sesh.query(State).order_by(State.id).all():
        print("{}: {}".format(row.id, row.name))
        for item in row.cities:
            print("    {}: {}".format(item.id, item.name))

    sesh.close()
