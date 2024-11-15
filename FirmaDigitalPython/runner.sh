python3 rsa_sign_verify.py sign "Test Message"

python3 rsa_sign_verify.py verify

python3 rsa_sign_verify.py verify --message text.txt --signature sign.bin --key pub_key.pem
