import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from xml.dom.minidom import parseString


# ------------- This Class prints the wanted tables of a given page IN HTML------------------
class PI(object):
    def __init__(self, report_par):
        self.report = report_par
        self.username = "nguyenhi"
        self.password = "dmcnbnB1i9e9n64"

    def main(self):
        # print report name
        print("Report for " + self.report)

        expandableContent = "&expand=body.storage"
        # get to the website of the wanted report
        response = requests.get(
            "https://confluence.diconium.com/rest/api/content?spacekey=Testmanagement&title=" + self.report + expandableContent,
            auth=HTTPBasicAuth(self.username, self.password))
        # store the full json data of the report
        json_data = response.json()
        # store the content of the report
        content_of_page = json_data['results'][0]['body']['storage']['value']

        # removed prefix ac and "&" symbol from the xml content of the website
        formatted = content_of_page.replace("ac:", "").replace("ri:", "").replace("&", "&amp;");

        # print pretty xml of the formatted content of the website
        content_dom = parseString(formatted)

        # 1.1 Status with its table content
        for element in content_dom.getElementsByTagName("h3"):
            if (element.firstChild.nodeValue == "1.1 Status"):
                print("Table title: " + element.firstChild.nodeValue)
                for row in element.nextSibling.getElementsByTagName("tr"):
                    print("-" * 5 + "row" + "-" * 5)
                    for header in row.getElementsByTagName("th"):
                        print(header.firstChild.nodeValue)
                    for data in row.getElementsByTagName("td"):
                        if data.firstChild.nodeName == "structured-macro":
                            farbe = "<DOM Text node "'Grey'">"
                            inhalt = str()
                            for parameter in data.firstChild.getElementsByTagName("parameter"):
                                if (str(parameter.attributes.item(0).value) == "colour"):
                                    farbe = str(parameter.firstChild)
                                elif (str(parameter.attributes.item(0).value) == "title"):
                                    inhalt = str(parameter.firstChild)
                            print(farbe + " " + inhalt)
                        elif data.firstChild.nodeName == 'p':
                            print(data.firstChild.firstChild.nodeValue)
                        else:
                            inhalt = str()
                            inhalt = (data.firstChild.nodeValue)
                            paramChild = data.firstChild
                            while str(paramChild.nextSibling) != "None":
                                paramChild = paramChild.nextSibling
                                # print(paramChild.nodeValue)
                                if (str(paramChild.nodeValue) != "None"):
                                    inhalt = inhalt + '. ' + str(paramChild.nodeValue);
                            print(inhalt)

                print(" ")