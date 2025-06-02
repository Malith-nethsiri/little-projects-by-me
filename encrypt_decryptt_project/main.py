import random
import string
from func import encrypting, decrypting

chars = string.ascii_letters + string.punctuation + " "
list_chars = list(chars)
keys = list_chars.copy()
encrypt_code = ""
massage = ""

random.shuffle(keys)

# encrypting
encrypt = input("Enter the massage you wanna encrypt -- ")

print(f"your massage -- {encrypt}")
print(f"your massage's encrypted code -- {encrypting(list_chars,keys,encrypt)}")
print()

# decrypting
decrypt_code = input("Enter the massage you wanna decrypt -- ")

print(f"your massage's encrypted code -- {decrypt_code}")
print(f"your massage -- {decrypting(list_chars,keys,decrypt_code)}")






