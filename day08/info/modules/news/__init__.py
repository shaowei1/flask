from flask import Blueprint

news_blue = Blueprint('news_blue', __name__)

# from use blueprint object import to create blueprint object
from . import view
