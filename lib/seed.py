#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, UserProfile, Permission, Role

if __name__ == '__main__':
    engine = create_engine('sqlite:///finalproject.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(UserProfile).delete()
    session.query(Permission).delete()
    session.query(Role).delete()

    fake = Faker()

#Data
users = [
    {
        "username": "Nehema Kinya",
        "email": "nehemakinya@gmail.com",
        "password": "12345",
    },
    {
        "username": "Purity Kawira",
        "email": "kawira@gmail.com",
        "password": "67897",
    },
]
user_profiles = [
    {
        "user_id": 1,
        "full_name": "Abel Mutua",
        "profile_picture": "profile1.jpg",
        "bio": "This is the bio of Abel Mutua.",
        "date_of_birth": 1994,
    },
    {
        "user_id": 2,
        "full_name": "Sammy Njoroge",
        "profile_picture": "profile2.jpg",
        "bio": "This is the bio of Sammy Njoroge.",
        "date_of_birth": 2000,
    },
]
permissions = [
    {
        "name": "read",
        "description": "Read permission",
    },
    {
        "name": "write",
        "description": "Write permission",
    },
]
roles = [
    {
        "name": "admin",
        "description": "Administrator role",
        "user_id": 1,
    },
    {
        "name": "user",
        "description": "Regular user role",
        "user_id": 2,
    },
]

# Add data to the database
for user_data in users:
    user = User(**user_data)
    session.add(user)

for profile_data in user_profiles:
    profile = UserProfile(**profile_data)
    session.add(profile)

for permission_data in permissions:
    permission = Permission(**permission_data)
    session.add(permission)

for role_data in roles:
    role = Role(**role_data)
    session.add(role)

# Commit the changes
session.commit()

# Close the session
session.close()
