from flask import Blueprint

speak = Blueprint('speak',__name__)
from app.speak import views