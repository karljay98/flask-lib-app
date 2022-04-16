from application import app, db
#from application.forms import TaskForm
#from application.models import Tasks
from flask import render_template #request, redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')
