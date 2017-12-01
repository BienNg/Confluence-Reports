import requests
from requests.auth import HTTPBasicAuth

class PutContent(object):

    def __init__(self, reports):
        self.reports = reports
        self.username = "nguyenhi"
        self.password = "dmcnbnB1i9e9n65"

        self.content = str()
        i = 0
        for report in reports:
            i += 1
            self.content += "<h3>1." + str(i)+ " " + report.report_name +"</h3>"\
                       + report.table.replace("&amp;nbsp;", "").replace("&amp;", "&")

    def put_content(self):
        # PageID of the "Übericht"-Page
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
                        "value": "<h2>1. Status</h2>"
                                 + self.content,
                        "representation":"storage"
                    }
                }
            }
        # get to the website of the wanted report
        response = requests.put(url, auth=HTTPBasicAuth(self.username, self.password), json=payload)
        print(response)
        print(response.text)
