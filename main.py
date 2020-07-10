from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

# generate and write a new key

# generate_key()
# load the previously generated key


def store_data(message,filename):
    message = "some secret message".encode()
    print("message: encrypted")
    print(message)
    key = load_key()
    # initialize the Fernet class
    f = Fernet(key)
    # encrypt the message
    encrypted = f.encrypt(message)
    with open(filename, "wb") as savefile:
        savefile.write(encrypted)

    # print how it looks
    print("encrypted: ", encrypted)


def decrypt_data(datafile):
    key = load_key()
    f = Fernet(key)
    with open(datafile, "rb") as file:
        encrypted=file.read()
    decrypted_encrypted = f.decrypt(encrypted)
    print("decrypted: ", decrypted_encrypted)


if __name__ == "__main__":
    store_data("message", "mydata.data")
    decrypt_data("mydata.data")
