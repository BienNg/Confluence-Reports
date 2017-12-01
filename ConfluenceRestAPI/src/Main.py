# -*- coding: utf-8 -*-
from src.PutContent import PutContent
from src.ReadContent import ReadContent
import getpass

""" This class starts the script
A reports list is created where all the wanted Confluence pages are stored.
Then this list is parsed to the PutContent class where the new Übersicht-Page is updated.
"""

# Access information
user = input("User: ")
psw = input("Password: ")
access = (user, psw)

# All tables that are listed in here are added to the Übersicht-Page if they exist
tables = [
    "1.1 Status",
    "1.2 Milestones"
]

# ReadContent(--X--, tables) adds a new Table to the Übersicht-Page
reports = [
    ReadContent("OWM - Teststatus", tables, access),
    ReadContent("Collection Teststatus", tables, access),
    ReadContent("MAR2020 - Teststatus", tables, access),
    ReadContent("ZBVSAPP Zeppelin Lead App-Teststatus", tables, access),
    ReadContent("ZEPPELIN FASTRENT - Release 1.0", tables, access)
]

PutContent(reports, access).put_content()