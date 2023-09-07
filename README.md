# User Authentication System

This is a simple User Authentication System project built with Python using SQLAlchemy and Faker.

## Description

The User Aunthentication System is designed to manage users, their profiles, permissions, and roles. It utilizes the SQLAlchemy library to interact with a SQLite database. The project demonstrates basic CRUD (Create, Read, Update, Delete) operations for users, user profiles, permissions, and roles.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python 3.x
- SQLAlchemy
- Faker

You can install the required Python packages using pip:

   pip install sqlalchemy faker

## Usage

## Initializing the Database

To initialize the database and populate it with data, run the following script:
   python initialize_database.py

This script creates an SQLite database named 'finalproject.db' and adds sample users, user profiles, permissions, and roles to it.

## Running the Application

You can run the main application to interact with the User Aunthentication System. Here's how to start it:
      python main.py

This will start the application, allowing you to perform CRUD operations on users, user profiles, permissions, and roles.

## Project Structure

'main.py': Main application script for interacting with the User Aunthentication System.
'models.py': Defines SQLAlchemy models for User, UserProfile, Permission, and Role.
'finalproject.db': SQLite database file.

## Acknowledgments

SQLAlchemy - A powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.
Faker - A Python library for generating fake data.

## Author

Nehema Kinya.


