#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
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

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for states containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the states
    for state in states_with_a:
        session.delete(state)

    # Commit the session to the database
    session.commit()

    # Close session
    session.close()
