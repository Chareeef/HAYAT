#!/usr/bin/python3
"""Initialize database storage"""
from db.engine.storage import Storage

# Create an instance of Storage
storage = Storage()

# Create tables and sqlalchemy session
storage.load_all()
