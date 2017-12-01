import requests
from requests.auth import HTTPBasicAuth
import json
from src.ContentInXML import ContentInXML

class PutContent(object):

    def __init__(self,content):
        self.content = content
        self.table = content.table.replace("&amp;nbsp;" , "")
        self.table_name = content.report
        self.username = "nguyenhi"
        self.password = "dmcnbnB1i9e9n65"

    def put_content(self):
        url = "https://confluence.diconium.com/rest/api/content/46874887"
        response = requests.get(url + "?expand=version",auth=HTTPBasicAuth(self.username, self.password))
        json_data = response.json()
        version = (json_data['version']['number'])


        payload = \
            {
                "version":{
                    "number":version+1
                },
                "title": "Übersicht",
                "type": "page",
                "body":{
                    "storage":{
                        "value":self.table,
                          "representation":"storage"
                    }
                }
            }
        #payload = {'type': 'page', 'title': 'new page',"ancestors":[{"id":46874887}],'space':{'key':'Testmanagement'},"body":{"storage":{'value':"<p>This is a new page</p>",'representation':'storage'}}}
        # get to the website of the wanted report
        response = requests.put(url, auth=HTTPBasicAuth(self.username, self.password), json=payload)
        print(response)
        print(response.text)
