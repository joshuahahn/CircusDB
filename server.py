#!/usr/bin/env python
# External IP Address: 35.190.152.67
"""
COMS W4111.003 Introduction to Databases
Project 1 Part 3
Joshua Hahn jyh2134
Kayla Poulsen kap2229
"""

# Necessary imports
import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, abort

import applications.staff_directory
import applications.acts
import applications.equipment
import applications.animals
import applications.add_employee

# Path to HTML templates
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

# URI to our database
DATABASEURI = "**********************************"

# Create engine to connect to database
engine = create_engine(DATABASEURI)

# Things to run before website is loaded
@app.before_request
def before_request():
  try:
    g.conn = engine.connect()
  except:
    print ("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

# Closing website
@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


# Initial landing page.
@app.route('/', methods = ["GET", "POST"])
def index():
  try:
    return render_template("login.html")
  except:
    abort(404)

@app.route('/login/', methods = ['GET', 'POST'])
def login():
  try:
    if "GET"==request.method:
      render_template("login.html")
    else:
      query = request.form
      if query['username'] == "admin" and query["password"] == "databases":
        return render_template("home.html")
      else:
        return render_template("wrong_login.html")
  except:
    abort(404)


# Wrong login page.
@app.route('/wrong_login/', methods = ["GET", "POST"])
def wrong_login():
  return render_template("wrong_login.html")

# When users create an error, it takes them to the error page.
# They can then access other pages and try again.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

# Renders the home page.
@app.route("/home/", methods = ["GET"])
def home_render():
  return render_template("home.html")

# Calls page to show all employees. Can either add or search employees.
@app.route("/staff_directory/", methods = ["GET","POST"])
def staff_directory_render(): 
  try:
    if "GET" == request.method: # If request is to GET information
      return render_template("staff_directory.html") 
    else:
      query = applications.staff_directory.fetch(request.form)
      cursor = g.conn.execute(query)
      result = []
      for c in cursor:
        result.append(c)
      return render_template("/lookup_view.html", **dict(lookup_result = result)) # Render template with this information
  except:
    abort(404)

# LookupView for equipment.
@app.route("/equipment_lookup/", methods = ["POST"])
def equipment_lookup():
  try:
    query = applications.equipment.fetch(request.form)
    cursor = g.conn.execute(query)
    result = []
    for c in cursor:
      result.append(c)
    return render_template("/lookup_view.html", **dict(lookup_result = result))
  except:
    abort(404)

# LookupView for animals.
@app.route("/animal_lookup/", methods = ["POST"])
def animal_lookup():
  try:
    query = applications.animals.fetch(request.form)
    cursor = g.conn.execute(query)
    result = []
    for c in cursor:
      result.append(c)
    return render_template("/lookup_view.html", **dict(lookup_result = result))
  except:
    abort(404)

# Calls page to show acts. Can either add or search acts.
@app.route("/acts/", methods = ["GET","POST"])
def acts_render():
  try:
    if "GET" == request.method:
      return render_template("acts.html") # Render the default acts.html page.
    else: # If the user executes a search, 
      query = applications.acts.fetch(request.form) # Get the query from the python file
      cursor = g.conn.execute(query) # Execute the query
      result = []
      for c in cursor:
        result.append(c)
      return render_template("/lookup_view.html", **dict(lookup_result = result)) # Load the lookup_view page.
  except:
    abort(404)

# Adding acts page.
@app.route("/add_acts/", methods = ["GET","POST"])
def add_act():
  try:
    if "POST" == request.method: # If we are POSTING information to our database,
      query = applications.acts.add_act(request.form) # Get the INSERT string using the request form.
      g.conn.execute(query) # Execute the INSERT 
      return render_template("home.html")
    else:
      return render_template("home.html") # If we are not POSTING, then redirect to home.
  except:
    abort(404)


# Calls page to show equipment. Can either add or search equipment.
@app.route("/equipment/", methods = ["GET","POST"])
def equipment_render():
  try:
    if "GET" == request.method:
      return render_template("equipment.html") # Render the default equipment.html page.
    else: # If the user executes a search, 
      query = applications.equipment.fetch(request.form) # Get the query from the python file
      cursor = g.conn.execute(query) # Execute the query
      result = []
      for c in cursor:
        result.append(c)
      return render_template("/lookup_view.html", **dict(lookup_result = result)) # Load the lookup_view page.
  except:
    abort(404)

# Adding acts page.
@app.route("/add_equipment/", methods = ["GET","POST"])
def add_equipment():
  try:
    if "POST" == request.method: # If we are POSTING information to our database,
      query = applications.equipment.add_equipment(request.form) # Get the INSERT string using the request form.
      g.conn.execute(query) # Execute the INSERT 
      return render_template("home.html")
    else:
      return render_template("home.html") # If we are not POSTING, then redirect to home.
  except:
    abort(404)

# Calls page to show acts. Can either add or search acts.
@app.route("/animals/", methods = ["GET","POST"])
def animals_render():
  try:
    if "GET" == request.method:
      return render_template("animals.html") # Render the default acts.html page.
    else: # If the user executes a search, 
      query = applications.animals.fetch(request.form) # Get the query from the python file
      cursor = g.conn.execute(query) # Execute the query
      result = []
      for c in cursor:
        result.append(c)
      return render_template("/lookup_view.html", **dict(lookup_result = result)) # Load the lookup_view page.
  except:
    abort(404)

# Adding animals page.
@app.route("/add_animal/", methods = ["GET","POST"])
def add_animal():
  try:
    if "POST" == request.method: # If we are POSTING information to our database,
      query = applications.animals.add_animal(request.form) # Get the INSERT string using the request form.
      g.conn.execute(query) # Execute the INSERT 
      return render_template("home.html")
    else:
      return render_template("home.html") # If we are not POSTING, then redirect to home.
  except:
    abort(404)

# Adding all employees page.
@app.route("/employee_add/", methods = ["GET","POST"])
def employee_add():
  try:
    return render_template("add_employee.html")
  except:
    abort(404)

# Adding employee page.
@app.route("/add_employee/", methods = ["GET", "POST"])
def add_employee():
  try:
    if "POST" == request.method:
      query = applications.add_employee.add_employee(request.form)
      g.conn.execute(query)
      return render_template("home.html")
    else:
      return render_template("home.html")
  except:
    abort(404)

# Adding performer page.
@app.route("/add_performer/", methods = ["GET", "POST"])
def add_performer():
  try:
    if "POST" == request.method:
      query = applications.add_employee.add_performer(request.form)
      g.conn.execute(query[0])
      g.conn.execute(query[1])
      return render_template("home.html")
    else:
      return render_template("home.html")
  except:
    abort(404)

# Adding choreographer page.
@app.route("/add_choreographer/", methods = ["GET", "POST"])
def add_choreographer():
  try:
    if "POST" == request.method:
      query = applications.add_employee.add_choreographer(request.form)
      g.conn.execute(query[0])
      g.conn.execute(query[1])
      return render_template("home.html")
    else:
      return render_template("home.html")
  except:
    abort(404)

# Adding animal trainer page.
@app.route("/add_animal_trainer/", methods = ["GET", "POST"])
def add_animal_trainer():
  try:
    if "POST" == request.method:
      query = applications.add_employee.add_animal_trainer(request.form)
      g.conn.execute(query[0])
      g.conn.execute(query[1])
      g.conn.execute(query[2])
      return render_template("home.html")
    else:
      return render_template("home.html")
  except:
    abort(404)

# Adding act page.
@app.route("/add_act/", methods = ["GET", "POST"])
def add_actr():
  try:
    if "POST" == request.method:
      query = applications.acts.add_act(request.form)
      g.conn.execute(query)
      return render_template("home.html")
    else:
      return render_template("home.html")
  except:
    abort(404)

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):

    HOST, PORT = host, port
    print ("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()