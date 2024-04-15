#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connection parameters
    username, password, db_name = sys.argv[1:]

    # Database engine creation
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for the state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Change the name to New Mexico if state with id=2 exists
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with id=2 not found")

    # Close session
    session.close()
