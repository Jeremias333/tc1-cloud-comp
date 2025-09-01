from flask import Flask
from .services.utils import make_respose

app = Flask(__name__)


@app.route('/')
def home():
    return make_respose({'message': 'Welcome to the API!'})


@app.route('/about')
def about():
    return make_respose({'message': 'This is a sample API built with Flask.'})


@app.route('/health')
def health():
    return make_respose({'status': 'OK'})