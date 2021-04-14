######################################################
# 
# Libraries
#
######################################################
import sys

from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
import requests
from bs4 import BeautifulSoup
import json
import helper

######################################################
# 
# App instance
#
######################################################

app = Flask(__name__)


######################################################
# 
# Routes
#
######################################################

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/intermediate')
def intermediate():
    return render_template('intermediate.html')

@app.route('/advance')
def advance():
    return render_template('advance.html')

@app.route('/expert')
def expert():
    return render_template('expert.html')


@app.route('/basicscrape')
def basicscrape():
    # flash(request.args.get('url'), 'success')
    url = request.args.get('url')

    try:
        # response = requests.get(url) // uncomment
        response = requests.get(url)
        content = BeautifulSoup(response.content, 'html.parser')
        resturantName = content.prettify()

        output = helper.basic_content(content)
    except:
        flash('Failed to retrieve URL "%s"' % url, 'danger')

    return render_template('basicscrape.html', content=resturantName, output=output)

@app.route('/intermediatescrape')
def intermediatescrape():
    # flash(request.args.get('url'), 'success')
    url = request.args.get('url')

    try:
        # response = requests.get(url) // uncomment
        response = requests.get(url)
        content = BeautifulSoup(response.content, 'html.parser')
        resturantName = content.prettify()

        output = helper.intermediate_content(content)
    except:
        flash('Failed to retrieve URL "%s"' % url, 'danger')

    return render_template('intermediatescrape.html', content=resturantName, output=output)

@app.route('/advancescrape')
def advancescrape():
    # flash(request.args.get('url'), 'success')
    url = request.args.get('url')

    try:
        # response = requests.get(url) // uncomment
        response = requests.get(url)
        content = BeautifulSoup(response.content, 'html.parser')
        resturantName = content.prettify()

        output = helper.advance_content(content)
    except:
        flash('Failed to retrieve URL "%s"' % url, 'danger')

    return render_template('advancescrape.html', content=resturantName, output=output)

@app.route('/expertscrape')
def expertscrape():
    # flash(request.args.get('url'), 'success')
    url = request.args.get('url')

    try:
        # response = requests.get(url) // uncomment
        response = requests.get(url)
        content = BeautifulSoup(response.content, 'html.parser')
        resturantName = content.prettify()

        output = helper.expert_content(content)
    except:
        flash('Failed to retrieve URL "%s"' % url, 'danger')

    return render_template('expertscrape.html', content=resturantName, output=output)


# render results to screen
@app.route('/results')
def results():
    args = []
    results = []

    for index in range(0, len(request.args.getlist('tag'))):
        args.append({
            'tag': request.args.getlist('tag')[index],
            'css': request.args.getlist('css')[index],
            'attr': request.args.getlist('attr')[index],
        })
    # print(args)
    response = requests.get(request.args.get('url'))
    content = BeautifulSoup(response.text, 'html.parser')

    # item to store scraped results
    item = {}

    # loop over request arguments
    for arg in args:
        # store item
        item[arg['css']] = [one.text for one in content.findAll(arg['tag'], arg['css'])]

    # loop over row indexes
    # print(len(item[next(iter(item))]))
    for index in range(0, len(item[next(iter(item))])):
        row = {}

        # loop over stored data
        for key, value in item.items():
            # append value to the new row
            row[key] = '"' + value[index] + '"'
        # print(row)
        # append new row to results list
        results.append(row)

    return render_template('results.html', results=results)


######################################################
# 
# Run app
#
######################################################

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True, threaded=True)
