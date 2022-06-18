from flask import Flask
feapp = Flask(__name__)

@feapp.route('/')
def hello_world():
    return 'sgeTestOne (my-feature-branch) says Hello, Docker!'
