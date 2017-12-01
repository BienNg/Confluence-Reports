# -*- coding: utf-8 -*-
import requests
import logging
from requests.auth import HTTPBasicAuth
from xml.dom.minidom import parseString
from xml.dom import expatbuilder

logging.basicConfig(filename='test.log', level=logging.DEBUG)

# ------------- This Class Reads the wanted Data of a given page IN HTML and stores them in a Table object------------------
class ReadContent(object):
    def __init__(self, report_name):
        self.report_name = report_name
        self.username = "nguyenhi"
        self.password = "dmcnbnB1i9e9n65"
        self.table = str()

        logging.debug("ReadContent.getTables() started")

        expandableContent = "&expand=body.storage"
        payload = {'spacekey':'Testmanagement', 'title':self.report_name.replace("&", "%26"), 'expand': 'body.storage'}
        url = "https://confluence.diconium.com/rest/api/content?spacekey=Testmanagement&title=" + self.report_name.replace("&", "%26") + expandableContent
        # get to the website of the wanted report
        response = requests.get(url,auth=HTTPBasicAuth(self.username, self.password))
        if response.status_code == 200:
            # store the full json data of the report
            json_data = response.json()
            # store the content of the report
            content_of_page = json_data['results'][0]['body']['storage']['value']

            # removed prefix ac and "&" symbol from the xml content of the website
            formatted = content_of_page\
                .replace("&auml;", "ä")\
                .replace("&ouml;", "ä")\
                .replace("&uuml;", "ü")\
                .replace("&", "&amp;")\
                ;

            # parse the formatted string to an xml dom object
            content_dom = expatbuilder.parseString(formatted, False)

            # reading 1.1 Status with its table content and store it to table
            for element in content_dom.getElementsByTagName("h3"):
                if (element.firstChild.nodeValue == "1.1 Status"):
                    self.table = element.nextSibling.toprettyxml()