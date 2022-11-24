from Crypto.Cipher import AES
import json

class crypto_dec:
    def getdec():
        with open('sectxt.json', 'rb') as f, open('k.txt', 'r') as k:
            dec_text = f.read()
            ke = json.loads(k.read())
            iv = ke["a"].replace("rmfs","ncc8").replace("optg","4auy").replace("lqwt","").replace("uydfg","").replace("krsvn","").encode('utf-8')
            key = ke["b"].replace("yql","0ie").replace("leh","fak").replace("hvd","").replace("kzr","").replace("iegwc","").encode('utf-8')
            cipher2 = AES.new(key, AES.MODE_CBC, iv)
            decryption_text = cipher2.decrypt(dec_text)
            text = decryption_text[:-decryption_text[-1]].decode('utf-8')
            json_text = json.loads(text)
        
        return json_text 