from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

RECAPTCHA_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
RECAPTCHA_SECRET_KEY_V2 = "6Lei2gcTAAAAAFl0MtXGr4iJ9n5Myb90gBnEK52H"
RECAPTCHA_SECRET_KEY_V2I = "6LfNBispAAAAAKSjVMRs35Zgnkjbt5bkjma7OAe3"
RECAPTCHA_SECRET_KEY_V3 = "6LfHBispAAAAACylyH2zYqbIGcSiWGCeZQubb3fr" 

HCAPTCHA_SECRET_KEY = "ES_ebcd95c6998546b1a77ba8a87b1e1e09"    # replace with your secret key
HCAPTCHA_VERIFY_URL = "https://api.hcaptcha.com/siteverify"

@app.get("/hello")
def hello():
    return "Hello World!!!"

@app.post("/api/hello2")
def hello2_api():
    result = {}
    if 'g-recaptcha-response' in request.form and len(request.form['g-recaptcha-response'])>0:
        data = { 'secret': RECAPTCHA_SECRET_KEY_V2, 'response': request.form['g-recaptcha-response'] }
        resp = requests.post(url=RECAPTCHA_VERIFY_URL, data=data)
        print(resp.json())
        result = {
            'msg': "Hello World v2"
        }
    return result

@app.post("/api/hello2i")
def hello2i_api():
    result = {}
    if 'g-recaptcha-response' in request.form and len(request.form['g-recaptcha-response'])>0:
        data = { 'secret': RECAPTCHA_SECRET_KEY_V2I, 'response': request.form['g-recaptcha-response'] }
        resp = requests.post(url=RECAPTCHA_VERIFY_URL, data=data)
        print(resp.json())
        result = {
            'msg': "Hello World v2i"
        }
    return result

@app.post("/api/hello3")
def hello3_api():
    result = {}
    if 'g-recaptcha-response' in request.form and len(request.form['g-recaptcha-response'])>0:
        data = { 'secret': RECAPTCHA_SECRET_KEY_V3, 'response': request.form['g-recaptcha-response'] }
        resp = requests.post(url=RECAPTCHA_VERIFY_URL, data=data)
        print(resp.json())
        result = {
            'msg': "Hello World v3"
        }
    return result

@app.post("/api/hhello")
def hhello_api():
    result = {}
    if 'h-captcha-response' in request.form and len(request.form['h-captcha-response'])>0:
        data = { 'secret': HCAPTCHA_SECRET_KEY, 'response': request.form['h-captcha-response'] }
        resp = requests.post(url=HCAPTCHA_VERIFY_URL, data=data)
        print(resp.json())
        result = {
            'msg': "Hello World Human"
        }
    return result

@app.post("/api/ahello")
def ahello_api():
    result = {}
    if 'h-captcha-response' in request.form and len(request.form['h-captcha-response'])>0:
        data = { 'secret': HCAPTCHA_SECRET_KEY, 'response': request.form['h-captcha-response'] }
        resp = requests.post(url=HCAPTCHA_VERIFY_URL, data=data)
        print(resp.json())
        result = {
            'msg': "Hello World2"
        }
    return result
