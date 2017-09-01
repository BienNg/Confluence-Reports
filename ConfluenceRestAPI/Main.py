import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import PageSummary

# print the wanted tables in html for Produkt Teststatus Template
ptt = PageSummary.PS("_Produkt-Teststatus Template")
ptt.main()

# print the wanted tables in html for Testreport Release 3.3
cat = PageSummary.PS("Testreport Release 3.3")
cat.main()
