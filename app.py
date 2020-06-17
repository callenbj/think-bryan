from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from model import InputForm, StateInputForm, CountyInputForm, ContactInputForm, ContactInputForm2
from flask import Flask, render_template, request
from covidlogic import sir_method, sir_method_contact
import sys
from wtforms import Form, FloatField, validators, StringField, ValidationError

import pymysql

import io
import os
import uuid
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

app = Flask(__name__, static_folder='D://think-bryan//static')
app.secret_key = 's3cr3t'
app.debug = True
#app._static_folder = os.path.abspath("templates/static/")
app._static_folder = os.path.abspath("static/")


@app.route('/', methods=['GET'])
def index():
    title = 'Home Screen'
    return render_template('layouts/index.html',
                           title=title)




@app.route('/covid', methods=['GET', 'POST'])
def vib2():
    #form = InputForm(request.form)
    user = 50

    form = ContactInputForm(request.form)
    form.A.data=396488
    if request.method == 'POST' and form.validate():

        #result = sir_method(form.A.data, form.b.data, form.w.data, form.T.data, form.R_0.data, form.D.data, form.C.data)
        result = sir_method_contact(form.A.data, form.b.data, form.w.data, form.T.data, form.R_0.data, form.D.data, form.C.data, form.CO.data, form.PP.data)
    else:
        result = None
        #print(form.message)
    template_name = 'view1'

    return render_template(template_name + '.html',
                           form=form, result=result)

@app.route('/catpictures', methods=['GET'])
def catpictures():
    title = 'Coming Soon'
    return render_template('layouts/catpictures.html',
                           title=title)


@app.route('/equations', methods=['GET'])
def equations():
    title = 'Equations and whatnot'
    return render_template('layouts/equations.html',
                           title=title)

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    app.run()
