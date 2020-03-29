from pymodm.connection import connect

from corona.settings import MONGO_URI

connect(MONGO_URI)
