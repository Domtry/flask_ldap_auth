from flask import Blueprint, jsonify, request
from src.ldap_handler import LdapServer

ldap_auth_bp = Blueprint("Authenticate", __name__, url_prefix="/api/v1/auth")


@ldap_auth_bp.post('/search')
def search():
    username = request.json['username']
    password = request.json['password']

    result = LdapServer.search_user(username, password)
    
    return jsonify({
            "message": "success operation", 
            "success": True, 
            "data": result
        }), 200