from flask import Blueprint

from ..models import SchoolFee

transaction = Blueprint('transaction', __name__)
from . import views, forms


