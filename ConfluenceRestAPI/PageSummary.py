import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


# ------------- This Class prints the wanted tables of a given page IN HTML------------------
class PS(object):
    def __init__(self, report_par):
        self.report = report_par

    def main(self):
        # --Todo-- delete
        #username = "nguyenhi"
        #password = "dmcnbnB1i9e9n64"

        username = input("Username: ")
        password = input("Password: ")

        # get to the website
        response = requests.get(
            "https://confluence.diconium.com/rest/api/content?spacekey=Testmanagement&title=" + self.report + "&expand=body.view",
            auth=HTTPBasicAuth(username, password))
        # get the json data
        json_data = response.json()

        # get the html text from the json
        html_text = json_data['results'][0]['body']['view']['value']

        soup = BeautifulSoup(str(html_text), 'html.parser')

        # print the table style
        print(table_style())
        # print name of the page
        print("<h2>Report: " + json_data['results'][0]['title'] + "</h2>")
        # get all the table_tags via the title
        table_tags = soup.find_all("h3")
        get_tables(table_tags)


# tables that are wanted
wanted_tables = ["Status", "Testdaten", "Gesamtübersicht", "Collection"]


# -------- Method that gets the table_tags and prints all tables that are wanted ---------
def get_tables(table_tags):
    # print all the table titles and their content
    for table in table_tags:
        for w_table in wanted_tables:
            if (w_table in table.string):
                table_body = table.next_sibling
                print(get_html(table))
                print(get_html(table_body))
    return []


# -------- Method that gets a html_text and returns the pretty html text--------------
def get_html(html_text):
    soup = BeautifulSoup(str(html_text), 'html.parser')
    return (soup.prettify())


# -------- Method that returns the style of the table ----------
def table_style():
    style = "</h3><style>table, th, td {border: 1px solid black;}</style>"
    return get_html(style)


# -------- Method that gets the title of the page ----------
def get_page_title(j_data):
    title = j_data['results'][0]['title']
    return title
