import os
import logging

from flask import Flask
from src.api import ldap_auth_bp
from src.ldap_handler import LdapServer

logging.basicConfig(
    filename='app.log', 
    filemode='+a', 
    format='[%(asctime)s]> %(name)s - %(levelname)s - %(message)s')  


def create_app():
    
    logging.getLogger('flask_cors').level = logging.DEBUG
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        FLASK_ENV = os.environ.get('FLASK_ENV'),
        FLASK_APP = os.environ.get('FLASK_APP'),
        SECRET_KEY = os.environ.get('SECRET_KEY'),
        FLASK_DEBUG = os.environ.get('FLASK_DEBUG'),
        FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST'),
        LDAP_HOST = os.environ.get('LDAP_HOST'),
        LDAP_BASE_DN = os.environ.get('LDAP_BASE_DN'),
        LDAP_USER_DN = os.environ.get('LDAP_USER_DN'),
        LDAP_GROUP_DN = os.environ.get('LDAP_GROUP_DN'),
        LDAP_USER_RDN_ATTR = os.environ.get('LDAP_USER_RDN_ATTR'),
        LDAP_BIND_USER_DN = None,
        LDAP_BIND_USER_PASSWORD = None,
    )

    LdapServer(app)
    app.register_blueprint(ldap_auth_bp)
    
    @app.after_request
    def add_header_response(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Content-Type', 'application/json')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Origin, Api-Credentiel-Key')
        return response   
          
    return app