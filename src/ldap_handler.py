from flask_ldap3_login import LDAP3LoginManager


class LdapServer:
    
    ldap_manager = None
    
    def __new__(cls, app_instance):
        if cls.ldap_manager is None:
            cls.ldap_manager = LDAP3LoginManager(app_instance) 
        return cls.ldap_manager
        
    @classmethod
    def search_user(cls, username, password=None):
        try: 
            return cls.ldap_manager.authenticate_search_bind(username, password)
        except Exception as e:
            print(e)
            return None