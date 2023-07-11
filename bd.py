import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("C:/dev/openpbl/openpbl.ai/versions/v5/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

bd = firestore.client()