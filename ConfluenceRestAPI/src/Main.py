# -*- coding: utf-8 -*-
from src.PutContent import PutContent
from src.Content import Content
from src.ContentInXML import ContentInXML

reports = [Content("_Produkt-Teststatus Template"),
           Content("ZEPPELIN FASTRENT - Release 1.0")
           , Content("ZBVSAPP Zeppelin Lead App-Teststatus")
           , Content("OWM - Teststatus")
           , Content("Collection & Accessoires - Teststatus")
           , Content("MAR2020 - Teststatus")]

reports = [ContentInXML("OWM - Teststatus")]
reports[0].getTables()

PutContent(reports[0].table).put_content()