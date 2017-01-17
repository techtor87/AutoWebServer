# import urllib.request
# import urllib.error
# import xml.dom.minidom

import requests
import json

base_url    = "http://cingetplm208pc.cloud.ge.com/oslc/cqrest/repo/7.1.1/db/"
return_type = "&rcm.contentType=application/json"
gets_base_url = "GETS/query/?rcm.name=Personal%20Queries/Missouri/"
rmd_base_url = "GETS/query/?rcm.name=Personal%20Queries/Missouri/"
cca_def_url = base_url + gets_base_url + "/CCA_Defects" + return_type
cca_scn_url = base_url + gets_base_url + "/CCA_SCNs" + return_type
rmd_def_url = base_url + gets_base_url + "/CCA_Defects" + return_type
rmd_scn_url = base_url + gets_base_url + "/CCA_SCNs" + return_type

username = 'gfaulconbridge'
pswd = '654321'

r = requests.get(cca_def_url, auth=(username, pswd))
json_data = json.loads(r.text)
for i in json_data['oslc_cm:results']:
    print(i)
