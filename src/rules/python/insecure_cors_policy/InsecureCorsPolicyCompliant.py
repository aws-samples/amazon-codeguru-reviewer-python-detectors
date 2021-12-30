# {fact rule=insecure-cors-policy@v1.0 defects=0}
from flask import app, request
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# Compliant: the send_wildcard is set to allow only a specific list of
# trusted domains.
CORS(app, origins=["*"], send_wildcard=False)
# {/fact}
