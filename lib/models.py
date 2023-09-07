from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(60), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

# # UserProfile model
class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'), unique=True, nullable=False)
    full_name = Column(String(100))
    profile_picture = Column(String(200))
    bio = Column(String())
    date_of_birth = Column(Integer())

    user = relationship('User', backref='profile', lazy=True)

# # Permission model
class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200))

# # Role model
class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column (String(200))

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # role_id = Column(Integer, ForeignKey('role.id'), nullable=False)

    user = relationship('User', backref='user_roles', lazy=True)
    # role = relationship('Role', backref='role_users', lazy=True)





   
   