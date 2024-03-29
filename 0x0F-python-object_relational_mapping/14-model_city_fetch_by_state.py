#!/usr/bin/python3
"""
    A script that prints all City objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    ses = Session()

    cities = ses.query(State, City) \
                    .filter(State.id == City.state_id)


    for city in cities:
        print("{}: ({}) {}".format(city.State.name, city.City.id, city.City.name))

    ses.close()
