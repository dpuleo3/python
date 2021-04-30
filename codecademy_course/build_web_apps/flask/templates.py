from flask import Flask
from helper import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  return '''
    <!DOCTYPE html>
    <html>
      <body>
        <h1>Cooking By Myself</h1>
        <p>Welcome to my cookbook. These are recipes I like.</p>
        <a href="/recipe/1">Fried Egg</a>
      </body>
    </html>
    '''

#### Add the variable `id` to the route URL
#### and make it the sole function parameter
@app.route("/recipe/<int:id>")
def recipe(id):
  return '''
    <!DOCTYPE html>
    <html>
      <body>
        <a href="/">Back To Recipe List</a>
        <p>names[id] = ''' + recipes[id] + '''</p>
        <p>descriptions[id] = ''' + descriptions[id] + '''</p>
        <p>ingredients[id] = ''' + str(ingredients[id]) + '''</p>
        <p>instructions[id] = ''' + str(instructions[id]) + '''</p>
      </body>
    </html>
    '''


# Rendering Templates
from flask import Flask, render_template
from helper import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  #### Return a rendered index.html file
  return render_template("index.html")

@app.route("/recipe/<int:id>")
def recipe(id):
  #### Return a rendered fried_egg.html file
  return render_template("fried_egg.html")


# Template Variables
from flask import Flask, render_template
from helper import recipes, descriptions, ingredients

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/recipe/<int:id>")
def recipe(id):
  #Add template variables as variable assignment arguments
  return render_template("recipe.html", template_recipe = recipes[id], template_description = descriptions[id], 
  template_ingredients = ingredients[id])

##recipe.html
<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe }}</h1>
    <p>{{ template_description }}</p>
    <h3>Ingredients</h3>
    <ul>
      <!-- Ingredients list elements
      should fill the <li> tags -->
      <li>{{template_ingredients[0]}}</li>
      <li>{{template_ingredients[1]}}</li>
      <li>{{template_ingredients[2]}}</li>
    </ul>
  </body>
</html>


# Variable Filters
# Jinja2 documentation: https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters
# title: Capitalizes the first letter of each word in a string, known as titlecase
# capitalize: Capitalizes the first character of a string, such as in a sentence
# lower/uppercase: Makes all the characters in a string lowercase/uppercase
# int/float: Changes any number variable to an integer/float
# default: Defines a default string if the variable is not defined
# length: Calculates the length of a string, list or dictionary variable
# dictsort: Sorts a dictionary by its keys
<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    # <!-- Make template_recipe title case -->
    <h1>{{ template_recipe | title }}</h1>
    # <!-- Ensure a default description -->  
    <p>{{ template_description | default("A " + template_recipe + " recipe.") }}</p>
    # <!-- Output number of ingredients --> 
    <h3>Ingredients {{ template_ingredients | length }}</h3>
    <ul>
      <li>{{ template_ingredients[0] }}</li>
      <li>{{ template_ingredients[1] }}</li>
      <li>{{ template_ingredients[2] }}</li>
    </ul>
    # <!-- Ensure sorted instruction dictionary -->
    <h3>Instructions</h3>
    <ol>
      <li>{{ template_instructions | dictsort }}</li>
    </ol>
  </body>
</html>


# If Statements
#  the default filter doesn’t work in this situation so an if statement is needed.
# Using if statements in a template happens inside a statement delimiter block: {% %}.
# Notice the {% endif %} delimiter is necessary to close the if statement.
# The condition can include a variable that is tested using standard comparison operators, <, >, <=, >=, ==, !=.
<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe | title }}</h1>
    # <!-- Insert description if statement here -->
    {% if template_description %}
    <p>{{ template_description }}</p>
    # <!-- Include else here -->
    {% else %}
    <p>A {{ template_recipe }} recipe.</p>
    # <!-- Be sure to close with an endif block -->
    {% endif %}
    <h3>Ingredients - {{ template_ingredients | length}}</h3>
    <ul>
      <li>{{ template_ingredients[0] }}</li>
      <li>{{ template_ingredients[1] }}</li>
      # <!-- Insert ingredient if statement -->
      {% if template_ingredients|length == 3 %}
      <li>{{ template_ingredients[2] }}</li>
      # <!-- Be sure to close with an endif block -->
      {% endif %}
    </ul>

    <h3>Instructions</h3>
    <ol>
      <li>{{ template_instructions | dictsort }}</li>
    </ol>
  </body>
</html>


# For Loops
# Iterate through a list variable:
# {% for element in template_list %}
# Iterate through a string:
# {% for char_in_string in “Hello!” %}
# Iterate through the keys of a dictionary variable:
# {% for key in template_dict %}
# Iterate through keys AND values of a dictionary with items():
# {% for key, value in template_dict.items() %}

<!DOCTYPE html> # recipe.html
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe | title }}</h1>
    
    {% if template_description %}
      <p>{{ template_description }}</p>
    {%else%}
      <p>A {{ template_recipe }} recipe.</p>
    {% endif %}
    
    <h3>Ingredients - {{ template_ingredients | length}}</h3>
    <ul>
      <!-- Implement a for loop to iterate through 
      `template_ingredients`-->
      {% for ingredient in template_ingredients %}
      <li>{{ ingredient }}</li>
      {% endfor %}
    </ul>

    <h3>Instructions</h3>
    <ul>
    {% for key, instruction in template_instructions|dictsort %}
      # <!-- Add the correct dictionary element to list 
      # the instructions -->
      <p>{{ key }}: {{ instruction }}</p>
    {% endfor %}
    </ul>
  </body>
</html>

<!DOCTYPE html> # index.html
<html>
  <body>
    <h1>Cooking By Myself</h1>
    <p>Welcome to my cookbook. These are recipes I like.</p>
    # <!-- Implement a for loop using `template_recipes`-->
    {% for id, name in template_recipes.items() %}
    <p><a href="/recipe/{{ id }}">{{ name }}</a></p>
    {% endfor %}
  </body>
</html>


# Inheritance
# To inherit this content in another template we will use the extends statement. 
# The code to be substituted should then be surrounded by {%block content%} and {%endblock%}

# base.html
<html>
  <body>
  {%block content%}{%endblock%} 
  </body>
</html>

# index.html
{% extends "base.html" %} # << ------- aqui esta llamando el contenido en base.html
{% block content %}  # < --- abriendo bloque a guardar
    <h1>Cooking By Myself</h1>
    <p>Welcome to my cookbook. These are recipes I like.</p>
    {% for id, name in template_recipes.items() %}
      <p><a href="/recipe/{{ id }}">{{ name | title }}</a></p>
    {% endfor %}
{% endblock %}  # < --- cerrando bloque a guardar