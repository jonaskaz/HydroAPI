"""Initialize the api namespaces"""
from flask_restx import Api

from .create_db import api as init_db_ns
from .ec_log import api as ec_log_ns
from .ph_log import api as ph_log_ns
from .temp_log import api as temp_log_ns
from .user import api as user_ns
from .level_log import api as level_log_ns
from .system_settings import api as system_settings_ns


api = Api(
    title="Hydro API",
    version="1.2",
    description="Hydroponics API to store and retrieve data on our Hydroponics system",
)


api.add_namespace(init_db_ns)
api.add_namespace(ec_log_ns)
api.add_namespace(ph_log_ns)
api.add_namespace(temp_log_ns)
api.add_namespace(user_ns)
api.add_namespace(level_log_ns)
api.add_namespace(system_settings_ns)
