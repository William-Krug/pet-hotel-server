import flask
import psycopg2
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def homePage():
  return "<h1>Welcome to the Pet Hotel<h1>"


app.run()