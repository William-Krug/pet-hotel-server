import flask
import psycopg2
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor

#export FLASK_APP=pageName.py
#python3 pageName.py

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def homePage():
  return "<h1>Welcome to the Pet Hotel<h1>"

@app.route('/owners', methods=['GET', 'POST'])
def api_owners():
  print("in /owners route")
  if request.method == 'POST':
    print("request.args", request.args)
    request_data = request.get_json()
    name = request_data['name']
    print("request_data", request_data)
   

    # name = request.json['body']['name']

    try:
      connection = psycopg2.connect(
      host="127.0.0.1",
      port="5432",
      database="pet_hotel"
      )
      cursor = connection.cursor(cursor_factory=RealDictCursor)
      sqlQuery = 'INSERT INTO "owners" ("name") VALUES (%s)'
      cursor.execute(sqlQuery, (name,))
      connection.commit()
      count = cursor.rowcount
      print(count, "Owner INSERTED")
      result = {'status': 'CREATED'}
      return make_response(jsonify(result), 201)
    except(Exception, psycopg2.Error) as error:
      if(connection):
        print("Failed to insert owner", error)
        result = {'status': 'ERROR'}
        return make_response(jsonify(result), 500)
    finally:
      if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
  else:
    connection = psycopg2.connect(
      host="127.0.0.1",
      port="5432",
      database="pet_hotel"
    )
    cursor = connection.cursor()
    sqlQuery = 'SELECT * FROM "owners"'
    cursor.execute(sqlQuery)
    data = cursor.fetchall()
    return jsonify(data)

app.run()