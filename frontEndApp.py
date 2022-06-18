from flask import Flask
feapp = Flask(__name__)

@feapp.route('/')
def hello_world():
    return 'myFrontEndService v1.2.3 says Hello, Docker!'
