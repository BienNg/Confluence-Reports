# -*- coding: utf-8 -*-
from src.PutContent import PutContent
from src.ReadContent import ReadContent

""" This is the starting class of the Script.
A reports list is created where all the wanted Confluence pages is stored.
Then this list is parsed to the PutContent class where the new Übersicht-Page is updated.
"""
# All tables that are listed in here are added to the Übersicht-Page if they exist
tables = [
    "1.1 Status",
    "1.2 Milestones"
]

# ReadContent(--X--, tables) adds a new Table to the Übersicht-Page
reports = [
    ReadContent("OWM - Teststatus", tables),
    ReadContent("Collection Teststatus", tables),
    ReadContent("MAR2020 - Teststatus", tables),
    ReadContent("ZBVSAPP Zeppelin Lead App-Teststatus", tables),
    ReadContent("ZEPPELIN FASTRENT - Release 1.0", tables)
]

PutContent(reports).put_content()