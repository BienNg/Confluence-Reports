# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from src.Controller import Controller

reports = [Controller("_Produkt-Teststatus Template"),
           Controller("ZEPPELIN FASTRENT - Release 1.0")
           , Controller("ZBVSAPP Zeppelin Lead App-Teststatus")
           , Controller("OWM - Teststatus")
           , Controller("Collection & Accessoires - Teststatus")]

reports = [Controller("OWM - Teststatus")]
for pi in reports:
    pi.getTables()