import requests
import logging
from requests.auth import HTTPBasicAuth

""" This class gets the wanted information of every report which was created by the ReadContent class and updates the Übersicht-Page in confluence.
"""
class PutContent(object):

    # This method is called when the class object is initialized.
    def __init__(self, reports):
        self.reports = reports
        self.username = ""
        self.password = ""

        # content contains the HTML of the Übersicht-Page
        self.content = str()
        i = 0
        for report in reports:
            i += 1
            self.content += "<h2>" + str(i)+ ". " + report.report_name +"</h2>"\
                       + report.table.replace("&amp;nbsp;", "").replace("&amp;", "&")

    # This method updated the Übersicht-Page
    def put_content(self):
        # This is the URL of the "Übericht"-Page
        url = "https://confluence.diconium.com/rest/api/content/46874887"

        # Request access to confluence with the username and password
        response = requests.get(url + "?expand=version",auth=HTTPBasicAuth(self.username, self.password))


        json_data = response.json()

        # Getting the current version of the Übersicht-Page
        version = (json_data['version']['number'])

        # Updating the new Übersicht-Page if the access information is right
        payload = \
            {
                "version":{
                    "number":version+1
                },
                "title": "Übersicht",
                "type": "page",
                "body":{
                    "storage":{
                        "value": self.content,
                        "representation":"storage"
                    }
                }
            }
        response = requests.put(url, auth=HTTPBasicAuth(self.username, self.password), json=payload)
        if(response == 200):
            logging.debug("PutContent.response = OK")
        else:
            print("PutContent.response.status_code != 200: Put Request Failed.")
