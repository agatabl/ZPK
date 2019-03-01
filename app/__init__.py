from flask_restplus import Api
from flask import Blueprint
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.area_controller import api as area_ns
from .main.controller.trail_controller import api as trail_ns
from .main.controller.map_controller import api as map_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API FOR ZPK_APP WITH JWT',
          version='1.0',
          description='API for ZPK_APP. Flask-restplus.'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(area_ns, path='/area')
api.add_namespace(trail_ns, path='/trail')
api.add_namespace(map_ns, path='/map')
api.add_namespace(auth_ns)
