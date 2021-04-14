# // Logic
import json
def basic_content(htmlContent):
    itemsArray = []
    rawData = {}

    # Rest Name
    resturantName = htmlContent.find('h1', class_='ec ed f6').text
    rawData["name"] = resturantName

    #  Categroy
    allCategories = htmlContent.findAll('li', class_='gc')

    for itemIndex, items in enumerate(allCategories):

        category = items.find('h2', class_='gd ge ce ea').text
        item = items.findAll('li', class_='gl gm gn ag')

        for unitIndex, unit in enumerate(item):
            itemDetails = []
            itemName = itemDesc = itemPrice = ''
            if (unit.find('div', class_='gt gu gv al')):
                itemName = unit.find('div', class_='gt gu gv al').text
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
                    itemDetails = {
                        slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}
            else:
                itemDetails = {slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}

            itemsArray.append(itemDetails)

    rawData['items'] = itemsArray
    return json.dumps(rawData, sort_keys=True, indent=4)

def intermediate_content(htmlContent):
    itemsArray = []
    rawData = {}

    # Rest Name
    resturantName = htmlContent.find('h1', class_='ec ed f6').text
    rawData["name"] = resturantName

    #  Categroy
    allCategories = htmlContent.findAll('li', class_='gb')

    for itemIndex, items in enumerate(allCategories):

        category = items.find('h2', class_='gc gd ce ea').text
        item = items.findAll('li', class_='gk gl gm ag')
        print(item)

        for unitIndex, unit in enumerate(item):
            itemDetails = []
            itemName = itemDesc = itemPrice = ''
            if (unit.find('div', class_='gs gt gu al')):
                itemName = unit.find('div', class_='gs gt gu al').text
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
                    itemDetails = {
                        slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}
            else:
                itemDetails = {
                    slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}

            itemsArray.append(itemDetails)

    rawData['items'] = itemsArray
    return json.dumps(rawData,sort_keys=True, indent=4)

def advance_content(htmlContent):
    itemsArray = []
    rawData = {}

    # Rest Name
    resturantName = htmlContent.find('h1', class_='ej ek g4').text
    rawData["name"] = resturantName

    #  Categroy
    allCategories = htmlContent.findAll('li', class_='hd')

    for itemIndex, items in enumerate(allCategories):

        category = items.find('h2', class_='he hf bg eh').text
        item = items.findAll('li', class_='hm hn ho ag')

        for unitIndex, unit in enumerate(item):
            itemDetails = []
            itemName = itemDesc = itemPrice = ''
            if (unit.find('div', class_='hu hv hw al')):
                itemName = unit.find('div', class_='hu hv hw al').text
            if (unit.find('div', class_='bx c5 dd ge')):
                itemDesc = unit.find('div', class_='bx c5 dd ge').text
            if (unit.find('div', class_='c4 bf dd ag')):
                itemPrice = unit.find('div', class_='c4 bf dd ag').text

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
                    itemDetails = {
                        slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}
            else:
                itemDetails = {
                    slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}

            itemsArray.append(itemDetails)

    rawData['items'] = itemsArray
    return json.dumps(rawData,sort_keys=True, indent=4)

def expert_content(htmlContent):
    itemsArray = []
    rawData = {}

    # Rest Name
    resturantName = htmlContent.find('h1', class_='ec ed g7').text
    rawData["name"] = resturantName

    #  Categroy
    allCategories = htmlContent.findAll('li', class_='ha')

    for itemIndex, items in enumerate(allCategories):

        category = items.find('h2', class_='hb hc ce ea').text
        item = items.findAll('li', class_='hj hk hl ag')
        for unitIndex, unit in enumerate(item):
            itemDetails = []
            itemName = itemDesc = itemPrice = ''
            if (unit.find('div', class_='hr hs ht al')):
                itemName = unit.find('div', class_='hr hs ht al').text
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
                    itemDetails = {
                        slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}
            else:
                itemDetails = {
                    slug: {"name": itemName, "desc": itemDesc, "price": itemPrice, "category": [category]}}

            itemsArray.append(itemDetails)

    rawData['items'] = itemsArray
    return json.dumps(rawData,sort_keys=True, indent=4)