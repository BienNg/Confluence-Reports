
import requests
from requests.auth import HTTPBasicAuth
from xml.dom.minidom import parseString
# for printing pretty xml texts
import xml.dom.minidom



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

    # print pretty xml of the formatted content of the website
    content_dom = parseString(formatted)


    # store the table into 'element'
    for element in content_dom.getElementsByTagName("h3"):
        if(element.firstChild.nodeValue == "1.1 Status"):
            print("Table title: " + element.firstChild.nodeValue)

            # Iterate through each row of the tabe
            for row in element.nextSibling.getElementsByTagName("tr"):
                print("-" * 5 + "row" + "-"*5)
                # print the headers of the tabe
                for header in row.getElementsByTagName("th"):
                    print(header.firstChild.nodeValue)
                #print the rows of the table
                for data in row.getElementsByTagName("td"):
                    if data.firstChild.nodeName == "structured-macro":
                        farbe = "<DOM Text node "'Grey'">"
                        inhalt = str()
                        for parameter in data.firstChild.getElementsByTagName("parameter"):
                            if(str(parameter.attributes.item(0).value) == "colour"):
                                farbe = str(parameter.firstChild)
                            elif (str(parameter.attributes.item(0).value) == "title"):
                                inhalt = str(parameter.firstChild)
                        print(farbe + " " +  inhalt)
                    elif data.firstChild.nodeName == 'p':
                            print(data.firstChild.firstChild.nodeValue)
                    else:
                        inhalt = str()
                        inhalt = (data.firstChild.nodeValue)
                        paramChild = data.firstChild
                        while str(paramChild.nextSibling) != "None":
                            paramChild = paramChild.nextSibling
                            #print(paramChild.nodeValue)
                            if(str(paramChild.nodeValue) != "None"):
                                inhalt = inhalt + '\n' + str(paramChild.nodeValue);
                        print(inhalt)

            print(" ")

    printPrettyXML(formatted)

# Prints pretty xml texts
def printPrettyXML(formatted):
    xml_tmp = xml.dom.minidom.parseString(formatted)
    print(xml_tmp.toprettyxml())


if __name__ == '__main__':
    #main()
    x = "HÄ"
    print(x.encode().decode())
