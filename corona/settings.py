import os

# Mongo
MONGO_HOST = os.environ.get("MONGO_HOST", "172.18.0.2")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
MONGO_DB = os.environ.get("MONGO_DB", "noosh")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "mongo")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "password")
MONGO_URI = (f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@"
             f"{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin")
