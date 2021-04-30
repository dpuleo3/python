# Flask Request Object
from flask import Flask, render_template, request
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  new_id = len(recipes) + 1
  if len(request.form) > 0:
    #### Add the recipe name to recipes[new_id] 
    recipes[new_id] = request.form["recipe"]
    #### Add the recipe description to descriptions[new_id]
    descriptions[new_id] = request.form["description"]
    #### Add the values to new_ingredients and new_instructions
    new_ingredients = request.form["ingredients"]
    new_instructions = request.form["instructions"]
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
  return render_template("index.html", template_recipes=recipes)

@app.route("/recipe/<int:id>")
def recipe(id):
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id])

@app.route("/about")
def about():
  return render_template("about.html")


# Route Selection
<!DOCTYPE html>
<html>
  <body>
    <div>
      # <!-- Replace URL string with url_for -->
      <a href="{{ url_for('index') }}">Recipes</a>
      | 
      # <!-- Replace URL string with url_for -->
      <a href="{{ url_for('about') }}">About</a>
    </div>
    {% block content %}
    {% endblock %}
  </body>
</html>

@app.route("/", methods=["GET", "POST"])
def index():
  return render_template("index.html", template_recipes=recipes)

@app.route("/about")
def about():
  return render_template("about.html")

# FlaskForm Class
from flask import Flask, render_template, request
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from flask_wtf import FlaskForm
# se esta heredando de esta carpeta para crear la clase
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

#### Create form class here
class CommentForm(FlaskForm): 
  comment = StringField("Comment") # is a 
  submit = SubmitField("Add Comment") # is a submit button

@app.route("/", methods=["GET", "POST"])
def index():
  return render_template("index.html", template_recipes=recipes)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  #### Instantiate form class here
  comment_form = CommentForm()
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], 
  template_ingredients=ingredients[id], template_instructions=instructions[id], template_comments=comments[id], 
  template_form=comment_form)

@app.route("/about")
def about():
  return render_template("about.html")


# Template Form Variables
{% extends "base.html" %}
{% block content %}
  <form method="POST">
  {{ template_form.hidden_tag() }}
  # <!-- Insert StringField elements here -->  
  {{ template_form.comment.label }}
  # comment input field
  {{ template_form.comment() }}
  # <!-- Insert SubmitField element here -->
  {{ template_form.submit() }}
  </form>
{% endblock %}

# Handling FlaskForm Data


# Validation
class CommentForm(FlaskForm):
  #### Add a validator argument in the StringField
  comment =  StringField("Comment")
  submit = SubmitField("Add Comment")
  validators = [StringField("Validator", validators = [DataRequired()])]

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm(csrf_enabled=False)
  #### Validation
  if comment_form.validate_on_submit():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)
  return render_template("recipe.html", template_recipe=recipes[id], 
  template_description=descriptions[id], template_ingredients=ingredients[id], 
  template_instructions=instructions[id], template_comments=comments[id], 
  template_form=comment_form)


# More Form Fields
class RecipeForm(FlaskForm):
  recipe_categories = [("Breakfast","Breakfast"), ("Lunch","Lunch"), ("Dinner","Dinner")]
  recipe = StringField("Recipe", validators=[DataRequired()])  
  #### Add `recipe_type` and assign it a new radio field instance
  recipe_type = RadioField("Type", choices = recipe_categories)
  description = StringField("Description")
  ingredients = TextAreaField("Ingredients")
  instructions = TextAreaField("Instructions")
  submit = SubmitField("Add Recipe")

  <table><tr>
      {% for btn in template_form.recipe_type %}
      <!-- Put the button variable then the button label 
      in the following td tags-->
      <td>{{ btn() }}</td>
      <td>{{ btn.label }}</td>
    {% endfor %}
    </tr></table>

@app.route("/", methods=["GET", "POST"])
def index():
  recipe_form = RecipeForm(csrf_enabled=False)
  if recipe_form.validate_on_submit():
    new_id = len(recipes)+1
    recipes[new_id] = recipe_form.recipe.data
    #### Add type data here
    types[new_id] = recipe_form.recipe_type.data 
    descriptions[new_id] = recipe_form.description.data
    new_ingredients = recipe_form.ingredients.data
    new_instructions = recipe_form.instructions.data
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
    comments[new_id] = []
  return render_template("index.html", template_recipes=recipes, template_form=recipe_form)


# Redirecting
@app.route('/', methods=["GET", "POST"])
def index():
  recipe_form = RecipeForm(csrf_enabled=False)
  if recipe_form.validate_on_submit():
    new_id = len(recipes)+1
    recipes[new_id] = recipe_form.recipe.data
    types[new_id] = recipe_form.recipe_type.data
    descriptions[new_id] = recipe_form.description.data
    new_igredients = recipe_form.ingredients.data
    new_instructions = recipe_form.instructions.data
    add_ingredients(new_id, new_igredients)
    add_instructions(new_id, new_instructions)
    comments[new_id] = []
    #### Redirect to recipe route here
    return redirect(url_for("recipe", id=new_id, _external=True, _scheme='https'))
  return render_template("index.html", template_recipes=recipes, template_form=recipe_form)


# Review

# How to access form data using the request object
# Control path selection with route function names using url_for()
# Create a web form structure using FlaskForm and WTForm fields
# Create a web form in the templates using FlaskForm variables
# Utilize field validators for increased data integrity
# Use redirect() to change paths easily within the app