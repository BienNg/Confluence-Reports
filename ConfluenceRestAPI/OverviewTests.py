import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from pprint import pprint


def main():
    username = "nguyenhi"
    password = "dmcnbnB1i9e9n64"
    report = "_Produkt-Teststatus Template"
    # get to the website
    response = requests.get(
        "https://confluence.diconium.com/rest/api/content?spacekey=Testmanagement&title=" + report + "&expand=body.view",
        auth=HTTPBasicAuth(username, password))
    # get the json data
    json_data = response.json()

    # get the html text from the json
    html_text = json_data['results'][0]['body']['view']['value']

    soup = BeautifulSoup(str(html_text), 'html.parser')
    # print name of the page
    print("<h2>Report: " + json_data['results'][0]['title'] + "</h2>")
    # get all the table_tags via the title
    table_tags = soup.find_all("h3")


if __name__ == '__main__':
    main()
