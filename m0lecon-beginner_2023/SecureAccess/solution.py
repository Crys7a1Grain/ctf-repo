import hashlib, json, base64

def generate_token(nonce: str):
    username = 'user001'
    secret = hashlib.sha256(username.encode() + nonce.encode()).hexdigest()
    bundle = {'user':username, 
     'secret':secret}
    return base64.b64encode(json.dumps(bundle).encode())

print(generate_token("EB831AFD-F0AB-4731-9054-5C71B11822B5"))