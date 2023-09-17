#!/usr/bin/python3
"""
    A script that lists all State objects from hbtn_0e_6_usa that conatin
    the letter a from teh database.
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    states = session.query(State).filter(State.name.ilike('%a%')) \
                    .order_by(State.id).all()

    # print states
    for s in states:
        print("{}: {}".format(s.id, s.name))

    session.close()