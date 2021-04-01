#!/usr/bin/python3
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

    add = State(name="California")
    add.cities = [City(name="San Francisco")]

    sesh.add(add)
    sesh.commit()

    sesh.close()
