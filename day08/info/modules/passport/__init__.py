from flask import Blueprint

passport_blue = Blueprint('passport_blue', __name__)

# from use blueprint object import to create blueprint object
from . import view
