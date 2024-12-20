import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir("files"):
    full_path = os.path.join("files", file)
    if os.path.isfile(full_path):
        files.append(file)

with open("Key.key", "rb") as key_:
    secret_key = key_.read()

for file in files:
    full_path = os.path.join("files", file)
    with open(full_path, "rb") as thefile:
        contents = thefile.read()
    contents_decrypthed = Fernet(secret_key).decrypt(contents) # Encrypth content of the file

    with open(full_path, "wb") as thefile:
        contents = thefile.write(contents_decrypthed)