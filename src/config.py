import os


class Settings:
    FLASK_DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY", default="foobar")
