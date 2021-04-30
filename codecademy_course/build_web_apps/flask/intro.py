from flask import Flask

app = Flask(__name__)


@app.route('/') # rutas
@app.route('/home') # rutas
def home():
    return '<h1>Hello, World!</h1>'

# ''' para multiples lineas de codigo HTML
@app.route('/reporter') # rutas
def reporter():
    return '''
    <h2>Reporter Bio</h2>
    <a href="/">Return to home page</a>
    '''

# When specifying the URL to bind to a view function, we have the option of making 
# any section of the path between the slashes (/) variable by indicating <variable_name>
# <int: 'elemento integer'>
# <float: 'elemento float'>

@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return f'''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''

@app.route('/article/<article_name>')
def article(article_name):
  return f'''
  <h2>{article_name.replace('-', ' ').title()}</h2>
  <a href='/'>Return back to home page</a>
  '''