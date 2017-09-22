
import requests
from requests.auth import HTTPBasicAuth
from xml.dom.minidom import parseString
# for printing pretty xml texts
import xml.dom.minidom
import xml.etree.ElementTree as ET



def main():
    # login information to get access to the confluence website
    username = "nguyenhi"
    password = "dmcnbnB1i9e9n64"
    report = "OWM - Teststatus"
    expandableContent = "&expand=body.storage"
    # get to the website of the wanted report
    response = requests.get(
        "https://confluence.diconium.com/rest/api/content?spacekey=Testmanagement&title=" + report + expandableContent,
        auth=HTTPBasicAuth(username, password))
    # store the full json data of the report
    json_data = response.json()
    #store the content of the report
    content_of_page = json_data['results'][0]['body']['storage']['value']

    # removed prefix ac and "&" symbol from the xml content of the website
    formatted =  content_of_page.replace("ac:", "").replace("&", "&amp;");


    root = ET.fromstring(formatted)
    print(root.tag)

    #printPrettyXML(formatted)

# Prints pretty xml texts
def printPrettyXML(formatted):
    xml_tmp = xml.dom.minidom.parseString(formatted)
    print(xml_tmp.toprettyxml())


if __name__ == '__main__':
    main()
