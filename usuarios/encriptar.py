from Crypto.Cipher import AES
import base64
import os

def codificar(email):
	BLOCK_SIZE = 32
	PADDING = '&'
 	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	secret = 'Mkkgc07nsxTnlzuuDUH63mAcfGZM7jMK'
	cipher = AES.new(secret)
	url = EncodeAES(cipher, email)
	return url
 
# decode the encoded string
def decodificar(url):
	BLOCK_SIZE = 32
	PADDING = '&'
 	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
 	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	secret = 'Mkkgc07nsxTnlzuuDUH63mAcfGZM7jMK'
	cipher = AES.new(secret)
	email = DecodeAES(cipher, url)
	return email

