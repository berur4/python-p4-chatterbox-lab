#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

from app import app
from models import db, Message

fake = Faker()

usernames = [fake.first_name() for _ in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    """Deletes existing messages and seeds the database with new messages."""
    
    print("Clearing existing messages...")
    Message.query.delete()
    db.session.commit()

    messages = [
        Message(body="Hello, world!", username="Alice"),
        Message(body="Flask is awesome!", username="Bob"),
        Message(body="React and Flask work great together!", username="Charlie"),
    ]

    # Generate 20 random messages
    for _ in range(20):
        message = Message(
            body=fake.sentence(),
            username=rc(usernames),
        )
        messages.append(message)

    db.session.add_all(messages)
    db.session.commit()
    print("Database seeded with messages!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables exist before seeding
        make_messages()
