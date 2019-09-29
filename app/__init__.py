from flask import Flask
from config import Config
import os

app = Flask(__name__)
basepath = os.path.abspath(".")
app.config.from_object(Config)

from app import routes
