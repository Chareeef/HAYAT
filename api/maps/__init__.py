from flask import Blueprint

blood_map = Blueprint('blood_map', __name__, url_prefix='/api')

from api.maps.blood_bag import *
from api.maps.city import *
from api.maps.country import *
from api.maps.donor import *
from api.maps.transfusion_center import *
