
import requests
from requests.auth import HTTPBasicAuth
import pprint



def main():
    # login information to get access to the confluence website
    username = "nguyenhi"
    password = "dmcnbnB1i9e9n65"
    report = "MMP / OWM / HEA - Teststatus"
    expandableContent = "&expand=body.storage"
    # get to the website of the wanted report
    response = requests.get(
        "https://confluence.diconium.com/rest/api/content?spacekey=Testmanagement&title=" + report + expandableContent,
        auth=HTTPBasicAuth(username, password))
    # store the full json data of the report
    json_data = response.json()
    #store the content of the report
    content_of_page = json_data['results'][0]['body']['storage']['value']
    pprint.pprint(content_of_page)

if __name__ == '__main__':
    main()
