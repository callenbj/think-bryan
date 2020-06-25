from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from model import InputForm, StateInputForm, CountyInputForm, ContactInputForm, ContactInputForm2, DataGenForm
from flask import Flask, render_template, request, make_response, send_file
from io import StringIO
import csv

from werkzeug.wrappers import Response
from covidlogic import sir_method, sir_method_contact, data_generator
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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 's3cr3t'
app.debug = True
#app._static_folder = os.path.abspath("templates/static/")
app._static_folder = os.path.abspath("static/")
tempvar = 'images/covid_formulas.png'
tempvar2 = 'images/uhuracat.jpg'

@app.route('/', methods=['GET'])
def index():
    title = 'About Me'
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

@app.route('/logisticregression', methods=['GET'])
def logisticregression():
    title = 'Logistic Regression'
    return render_template('layouts/logisticregression.html',
                           title=title)

@app.route('/datagenerator', methods=['GET', 'POST'])
def datagenerator():
    title = 'Randomized Data Generator'
    form = DataGenForm(request.form)

    if request.method == 'POST' and form.validate():

        #result = sir_method(form.A.data, form.b.data, form.w.data, form.T.data, form.R_0.data, form.D.data, form.C.data)
        result = data_generator(form.A.data, form.MA.data, form.P.data, form.PF.data, form.NF.data)
        tempvar = result
        return send_file(result, as_attachment=True, cache_timeout=0)
    else:
        result = None
        #print(form.message)
    template_name = 'layouts/datagenerator'

    return render_template(template_name + '.html',
                           form=form, result=result)

@app.route('/catpictures', methods=['GET'])
def catpictures():
    title = 'Cat picture of the day'

    plotfile = os.path.join('images', 'ucat' + '.png')

    result = os.path.join('images', 'ucat' + '.png')

    #template_name = 'layouts/catpictures.html'
    template_name = 'view4.html'
    return render_template(template_name,
                           title=title, result=result)


@app.route('/equations', methods=['GET'])
def equations():
    title = 'Equations and References'
    return render_template('layouts/equations.html',
                           title=title)

@app.route('/download')
def download(self):
    si = StringIO.StringIO()
    cw = csv.writer(si)
    csvList = [5]
    cw.writerows(csvList)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output




@app.route('/download2')
def download_file2():
    #path = "html2pdf.pdf"
    #path = "info.xlsx"
    #path = "images/covid_formulas.png"
    #path = data_generator(5)
    path = tempvar
    #path = "sample.txt"
    return send_file(path, as_attachment=True, cache_timeout=0)


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    app.run()
