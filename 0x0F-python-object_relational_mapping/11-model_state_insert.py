#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connection parameters
    username, password, db_name = sys.argv[1:]

    # Database engine creation
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create Louisiana state object
    louisiana = State(name="Louisiana")

    # Add Louisiana to the session
    session.add(louisiana)

    # Commit the session to the database
    session.commit()

    # Print the new states.id after creation
    print(louisiana.id)

    # Close session
    session.close()
