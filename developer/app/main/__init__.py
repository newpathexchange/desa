from flask_smorest import Blueprint

print("Init main")
# Blueprint
blp = Blueprint(
    'desa', __name__, url_prefix='/api',
    description='DESA exercise API operations'
)

from . import k8s_probes
from . import exercise
