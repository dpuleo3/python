from flask import Flask
# para importar el diccionario 'pets' de la carpeta 'helper'
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href= '/animals/dogs'>Dogs</a></li>
    <li><a href= '/animals/cats'>Cats</a></li>
    <li><a href= '/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = '<h1>List of {pet_type}</h1>'
  for pet_type in pets:
    pet = '<li>{pet_type}</li>'
  return html + pet

@app.route('/animals/<pet_type>/int:<pet_id>')
def pet(pet_id):





