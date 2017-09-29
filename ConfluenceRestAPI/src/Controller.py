# -*- coding: utf-8 -*-
import requests
from idna import unicode
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from xml.dom.minidom import parseString
from xml.etree import ElementTree


# Class that represents a Table Instance
class Table(object):
    def __init__(self, table_name):
        self.table_name = table_name
        self.table = list()

    def __add_data__(self, content, row, column, color = None):
        if color == None:
            self.table[row].append(Cell(content))
            self.table[row][column].__print_content__()
        else:
            self.table[row].append(Cell(content, color))
            self.table[row][column].__print_content__()


    def __add_row__(self):
        self.table.append(list())

# Class that represents a Cell of a table
class Cell(object):
    def __init__(self, content, color = None):
        if color == None:
            self.content = content
            self.hasColor = False
        else:
            self.content = content
            self.color = color
            self.hasColor = True

    def __print_content__(self):
        if self.hasColor:
            print("This cell contains: " + self.content + " with the color: " + self.color)
        else:
            print("This cell contains " + self.content)


# ------------- This Class prints the wanted tables of a given page IN HTML------------------
class Controller(object):
    def __init__(self, report_par):
        self.report = report_par
        self.username = "nguyenhi"
        self.password = "dmcnbnB1i9e9n64"
        self.table = Table(report_par)

    def getTables(self):
        print("X"*500)
        # print report name
        print("Report for " + self.report)

        expandableContent = "&expand=body.storage"
        url = "https://confluence.diconium.com/rest/api/content?spacekey=Testmanagement&title=" + self.report.replace("&", "%26") + expandableContent
        # get to the website of the wanted report
        response = requests.get(url,auth=HTTPBasicAuth(self.username, self.password))

        if response.status_code == 200:
            # store the full json data of the report
            json_data = response.json()
            # store the content of the report
            content_of_page = json_data['results'][0]['body']['storage']['value']

            # removed prefix ac and "&" symbol from the xml content of the website
            formatted = content_of_page.replace("ac:", "")\
                .replace("&auml;", "ä")\
                .replace("&ouml;", "ä")\
                .replace("&uuml;", "ü")\
                .replace("ri:", "")\
                .replace("&", "&amp;")\
                ;

            # parse the formatted string to an xml dom object
            content_dom = parseString(formatted)

            # 1.1 Status with its table content
            for element in content_dom.getElementsByTagName("h3"):
                if (element.firstChild.nodeValue == "1.1 Status"):
                    # Initialize a new Table
                    table = Table(element.firstChild.nodeValue)
                    print("Table title: " + table.table_name)
                    r = 0
                    for row in element.nextSibling.getElementsByTagName("tr"):
                        table.__add_row__()
                        c = 0
                        print("-" * 5 + "row " + str(r) + "-" * 5)
                        for header in row.getElementsByTagName("th"):
                            content = header.firstChild.nodeValue
                            table.__add_data__(content, r, c)
                            c += 1
                        for data in row.getElementsByTagName("td"):
                            hasColor = False
                            for tags in data.getElementsByTagName("structured-macro"):
                                hasColor = True
                                farbe = "<DOM Text node Grey>"
                                content = str()
                                for parameter in tags.getElementsByTagName("parameter"):
                                    if (str(parameter.attributes.item(0).value) == "colour"):
                                        farbe = str(parameter.firstChild)
                                    elif (str(parameter.attributes.item(0).value) == "title"):
                                        content = str(parameter.firstChild)
                                table.__add_data__(content, r, c, farbe)
                            if hasColor:
                                # Table Data has color
                                hasColor = False
                            elif data.firstChild.nodeName == 'p':
                                content = data.firstChild.firstChild.nodeValue
                                paramChild = data.firstChild.firstChild
                                while str(paramChild.nextSibling) != "None":
                                    paramChild = paramChild.nextSibling
                                    if (str(paramChild.nodeValue) != "None"):
                                        content = content + '. ' + str(paramChild.nodeValue);
                                table.__add_data__(content, r, c)
                            else:
                                content = data.firstChild.nodeValue
                                paramChild = data.firstChild
                                while str(paramChild.nextSibling) != "None":
                                    paramChild = paramChild.nextSibling
                                    if (str(paramChild.nodeValue) != "None"):
                                        content = content + '. \n' + str(paramChild.nodeValue);
                                table.__add_data__(str(content), r, c)
                            c += 1
                        r += 1

            #print(content_dom.toprettyxml())