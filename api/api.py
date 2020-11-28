from .server import *
from flask import Flask
from contextlib import redirect_stdout
import io
import random
from flask_cors import cross_origin

app = Flask(__name__, static_folder='../build', static_url_path='/')

f = io.StringIO()
with redirect_stdout(f):
    import this
s = f.getvalue()
s1 = s.split("\n")[2:21]


# This doesn't need authentication
@app.route("/api/public")
@cross_origin(headers=["Content-Type", "Authorization"])
def public():
    response = "Hello from a public endpoint! You don't need to be" \
               " authenticated to see this."
    return jsonify(message=response)


# This needs authentication
@app.route("/api/private")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private():
    response = "Hello from a private endpoint! You need to be authenticated" \
               " to see this."
    return jsonify(message=response)


# This needs authorization
@app.route("/api/private-scoped")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private_scoped():
    if requires_scope("read:messages"):
        response = "Hello from a private endpoint! You need to be " \
                   "authenticated and have a scope of read:messages to see" \
                   " this."
        return jsonify(message=response)
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)


@app.route('/')
@cross_origin(headers=["Content-Type", "Authorization"])
def index():
    return app.send_static_file('index.html')


# This doesn't need authentication
@app.route('/api/zen')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_random_zen():
    return {'zen': random.choice(s1)}


# This needs authorization
@app.route('/api/zensec')
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_random_zen_sec():
    if requires_scope("read:messages"):
        return {'zensec': random.choice(s1)}
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)
