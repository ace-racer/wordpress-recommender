import os

DATA_LOC = os.getenv("DATA_LOC", "./data")

if not os.path.exists(DATA_LOC):
    os.makedirs(DATA_LOC)
