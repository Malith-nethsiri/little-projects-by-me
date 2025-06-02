#functions
def encrypting(list_chars,keys,encrypt):
     return "".join([keys[list_chars.index(e_letter)] for e_letter in encrypt])

def decrypting(list_chars,keys,decrypt_code):
    return "".join([list_chars[keys.index(d_letter)] for d_letter in decrypt_code])