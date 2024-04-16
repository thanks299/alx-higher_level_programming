#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Query for states and cities, sorted by state id and city id
    states_cities = session.query(
            State, City).join(City).order_by(State.id, City.id).all()

    # Print results
    for state, city in states_cities:
        if city == state.cities[0]:  # Only print state name once
            print("{}: {}".format(state.id, state.name))
        print("\t{}: {}".format(city.id, city.name))

    # Close session
    session.close()
