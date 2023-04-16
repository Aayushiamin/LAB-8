"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import inspect
from random import choice, randint 
import sqlite3
from datetime import datetime
from faker  import Faker

fake = Faker()

# Determine the path of the database
def main():

    db_path = os.path.join(os.path.dirname(os.path.abspath()), 'social_network.db')
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    # TODO: Function body
    create_relationships_tbl_query = """
        CREATE TABLE IF NOT EXISTS relationships
        (
        id          INTEGER PRIMARY KEY,
        person1_id  INTEGER NOT NULL,
        person2_id  INTEGER NOT NULL,
        type        TEXT NOT NULL,
        start_date  DATE NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people (id),
        FOREIGN KEY (person2_id) REFERENCES people (id)
        );
    """
    cur.execute(create_relationships_tbl_query)
    con.commit()
    con.close()

    return

def populate_relationships_table():

    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    add_relationship_query = """
        INSERT INTO relationships
        (
        person1_id,
        person2_id,
        type,
        start_date
        )
        VALUES (?, ?, ?, ?);
    """
    # Randomly select first person in relationship
    person1_id = randint(1, 200)
# Randomly select second person in relationship
# Loop ensures person will not be in a relationship with themself
    person2_id = randint(1, 200)
    while person2_id == person1_id:
        person2_id = randint(1, 200)
# Randomly select a relationship type
    rel_type = choice(('friend', 'spouse', 'partner', 'relative'))
# Randomly select a relationship start date between now and 50 years ago
    start_date = fake.date_between(start_date='-50y', end_date='today')
# Create tuple of data for the new relationship
    new_relationship = (person1_id, person2_id, rel_type, start_date)
# Add the new relationship to the DB
    cur.execute(add_relationship_query, new_relationship)
    con.commit()
    con.close()
    return 

if __name__ == '__main__':
   main()