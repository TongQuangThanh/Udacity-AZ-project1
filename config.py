import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storageaccountproject1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'dI9AB7ATZUkStMTxuLd4XfXK1jiw7cIMgyf1oes2sUNFXcWU3RmRE/sp3fXWZz/EmCJ9UEcl8W9++AStxRM5jQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'project1thanhtq4server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'project_1_db_name'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'thanhtq4'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Quangthanh94'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = "Zuk8Q~kQovDa5U8AjckXh.LS6MYuWi_te0-vtbEk"

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "72dd5e4c-7f9a-43ad-b0ec-13b3a2c7ce57"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session


# project1thanhtq4server.database.windows.net

# project_1_db_name

# storageaccountproject1

# dI9AB7ATZUkStMTxuLd4XfXK1jiw7cIMgyf1oes2sUNFXcWU3RmRE/sp3fXWZz/EmCJ9UEcl8W9++AStxRM5jQ==

# images 

# Zuk8Q~kQovDa5U8AjckXh.LS6MYuWi_te0-vtbEk