#!/usr/bin/python3
"""
    A script that changes teh name of a State object in hbtn_0e_6_usa

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

    ses = Session()

    rename_state = ses.query(State) \
                          .filter(State.id == 2).first()
    rename_state.name = 'New Mexico'
    ses.commit()

    ses.close()
