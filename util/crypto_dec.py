from Crypto.Cipher import AES
import json
# import os

# echo $SHELL
# vim ~/.bash_profile
# export HACKATHO_CHATAPP_IV=eelqwta1foptgdfgdfa1ekrsvrmfs8
# source ~/.bash_profile

class crypto_dec:
    def getdec():
        iv = 'eea1f4adfa1ecc88'.encode('utf-8')
        # iv_old = os.getenv('HACKATHO_CHATAPP_IV').replace("rmfs","ncc8").replace("optg","4auy").replace("lqwt","").replace("uydfg","").replace("krsvn","")
        # iv = iv_old.encode('utf-8')

        with open('sectxt.json', 'rb') as f, open('k.txt', 'r') as k:
            dec_text = f.read()
            ke = k.read().replace("yql","0ie").replace("leh","fak").replace("hvd","").replace("kzr","").replace("iegwc","")
            dec_key = ke.encode('utf-8')
            cipher2 = AES.new(dec_key, AES.MODE_CBC, iv)
            decryption_text = cipher2.decrypt(dec_text)
            text = decryption_text[:-decryption_text[-1]].decode('utf-8')
            json_text = json.loads(text)
        
        return json_text 