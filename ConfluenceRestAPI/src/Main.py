# -*- coding: utf-8 -*-
from src.PutContent import PutContent
from src.ReadContent import ReadContent

""" This is the starting class of the Script.
A reports list is created where all the wanted Confluence pages is stored.
Then this list is parsed to the PutContent class where the new Übersicht-Page is updated.
"""

# ReadContent(X) adds a new Table to the Übersicht-Page
reports = [
    ReadContent("OWM - Teststatus"),
    ReadContent("Collection Teststatus"),
    ReadContent("MAR2020 - Teststatus"),
    ReadContent("ZBVSAPP Zeppelin Lead App-Teststatus"),
    ReadContent("ZEPPELIN FASTRENT - Release 1.0")
]

PutContent(reports).put_content()