from flask import Flask
from contextlib import redirect_stdout
import io
import random

app = Flask(__name__, static_folder='../build', static_url_path='/')

f = io.StringIO()
with redirect_stdout(f):
    import this
s = f.getvalue()
s1 = s.split("\n")[2:21]


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/zen')
def get_random_zen():

    return {'time': random.choice(s1)}
