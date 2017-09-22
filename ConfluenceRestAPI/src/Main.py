import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from src.GetPageInformation import PI

# _Produkt-Teststatus Template
ptt = PI("_Produkt-Teststatus Template")
ptt.main()

# ZEPPELIN FASTRENT - Release 1.0"
zfr1 = PI("ZEPPELIN FASTRENT - Release 1.0")
zfr1.main()

# ZBVSAPP Zeppelin Lead App-Teststatus
zzlat = PI("ZBVSAPP Zeppelin Lead App-Teststatus")
zzlat.main()

# OWM - Teststatus
omw = PI("OWM - Teststatus")
omw.main()