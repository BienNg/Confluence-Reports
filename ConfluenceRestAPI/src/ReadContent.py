# -*- coding: utf-8 -*-
import requests
import logging
from requests.auth import HTTPBasicAuth
from xml.dom import expatbuilder

logging.basicConfig(filename='test.log', level=logging.DEBUG)

"""This class gets the name of the wanted page (report_name), reads the content and stores the Status table.
"""
class ReadContent(object):

    # This method is called when the class object is initialized.
    def __init__(self, report_name, tables):
        self.username = "nguyenhi"
        self.password = "dmcnbnB1i9e9n65"
        self.report_name = report_name
        self.tables = tables

        # In the table variable the status table of the report is stored.
        self.table = str()

        logging.debug("ReadContent.getTables() of " + self.report_name +" started")

        # Storage needs to be extended. This is where the content of the page is shown.
        expandableContent = "&expand=body.storage"

        # This URL contains the content of the given page
        url = "https://confluence.diconium.com/rest/api/content?spacekey=Testmanagement&title=" + self.report_name.replace("&", "%26") + expandableContent

        # Request access to confluence with the username and password
        response = requests.get(url,auth=HTTPBasicAuth(self.username, self.password))

        # checking of the request is ok(200)
        if response.status_code == 200:

            # Store the full json data of the report in json_data
            json_data = response.json()

            # Storing the content of the report
            content_of_page = json_data['results'][0]['body']['storage']['value']

            # Removing prefix ac and "&" symbol from the xml content of the website
            formatted = content_of_page\
                .replace("&auml;", "ä")\
                .replace("&ouml;", "ä")\
                .replace("&uuml;", "ü")\
                .replace("&", "&amp;")\
                ;

            # Parsing the formatted string to an xml dom object
            content_dom = expatbuilder.parseString(formatted, False)

            # Iterating through all headlines to look for the wanted tables
            for element in content_dom.getElementsByTagName("h3"):

                for table in tables:

                    # Searching for the wanted table
                    if (element.firstChild.nodeValue == table):
                        # If name of the table is found, the table itself is stored as XML in the variable table
                        self.table += "<h3>" + table + "</h3>"+ element.nextSibling.toprettyxml()