# -*- coding: utf-8 -*-
from src.PutContent import PutContent
from src.ReadContent import ReadContent

reports = [ReadContent("OWM - Teststatus"), ReadContent("Collection Teststatus"),
           ReadContent("MAR2020 - Teststatus"), ReadContent("ZBVSAPP Zeppelin Lead App-Teststatus"),
           ReadContent("ZEPPELIN FASTRENT - Release 1.0")]

PutContent(reports).put_content()