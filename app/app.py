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

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/scrape')
def scrape():
    # flash(request.args.get('url'), 'success')
    url = request.args.get('url')

    try:
        # response = requests.get(url) // uncomment
        response = requests.get(
            'https://www.ubereats.com/miami/food-delivery/finka-table-%26-tap/hYHqDrZVRYucwE35gn3jAA?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk1pYW1pJTIwSW50ZXJuYXRpb25hbCUyMEFpcnBvcnQlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKd1VxNVRrMjMyWWdSNGZpaXktRGFuNWclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMjUuNzk1MzUyNSUyQyUyMmxvbmdpdHVkZSUyMiUzQS04MC4yNzg2NzY4JTdE')
        content = BeautifulSoup(response.content, 'html.parser')
        resturantName = content.prettify()

        # // Logic
        def json_praser(htmlContent):
            itemsArray = []
            rawData = {}

            # Rest Name
            resturantName = htmlContent.find('h1', class_='ec ed g7').text
            rawData["name"] = resturantName

            #  Categroy
            allCategories = htmlContent.findAll('li', class_='h5')

            for itemIndex, items in enumerate(allCategories):

                category = items.find('h2', class_='h6 h7 ce ea').text
                item = items.findAll('li', class_='he hf hg ag')

                for unitIndex, unit in enumerate(item):
                    itemDetails = []
                    itemName = itemDesc = itemPrice = ''
                    if (unit.find('div', class_='hm hn ho al')):
                        itemName = unit.find('div', class_='hm hn ho al').text
                    if (unit.find('div', class_='cc dw cr ct')):
                        itemDesc = unit.find('div', class_='cc dw cr ct').text
                    if (unit.find('div', class_='cw cq cr ag')):
                        itemPrice = unit.find('div', class_='cw cq cr ag').text

                    slug = "".join(itemName.lower().split())

                    if (len(itemsArray) > 0):
                        check = False
                        for index, element in enumerate(itemsArray):
                            for ele in element:
                                if (ele == slug):
                                    check = True
                                    itemDetails = []
                                    itemsArray[index][slug]["category"].append(category)
                                    break
                                else:
                                    check = False
                            if (check):
                                break
                        if (not check):
                            itemDetails = {slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}
                    else:
                        itemDetails = {slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}
                    
                    itemsArray.append(itemDetails)

            rawData['items'] = itemsArray
            return json.dumps(rawData)

        output = json_praser(content)
    except:
        flash('Failed to retrieve URL "%s"' % url, 'danger')

    return render_template('scrape.html', content=resturantName, output=output)


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
