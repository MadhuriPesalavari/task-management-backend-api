import os

class Config:

    SQLALCHEMY_DATABASE_URI = \
    "postgresql://postgres:password@localhost/taskdb"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "mysecretkey"