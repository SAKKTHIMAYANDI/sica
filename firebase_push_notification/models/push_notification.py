import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/home/sakkthi/private/odoo15/custom_addons/firebase_push_notification/data/serviceAccountKey.json")
# cred = credentials.Certificate("/opt/odoo15/SICAWeb/firebase_push_notification/data/serviceAccountKey.json")

# Only initialize Firebase if not already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
