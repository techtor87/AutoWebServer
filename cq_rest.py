from consts import consts
import requests
import json
from scn_data import scn_data_class
from def_data import defect_data_class

base_url = "http://cingetplm208pc.cloud.ge.com/oslc/cqrest/repo/7.1.1/db/"
return_type = "&oslc_cm.pageSize=300&rcm.contentType=application/json"
gets_base_url = "GETS/query/?rcm.name=Personal%20Queries/" + consts.proj_name_str
rmd_base_url = "RMD/query/?rcm.name=Personal%20Queries/" + consts.proj_name_str
cca_def_url = base_url + gets_base_url + "/CCA_Defects" + return_type
cca_scn_url = base_url + gets_base_url + "/CCA_SCNs" + return_type
rmd_def_url = base_url + rmd_base_url + "/RMD_Defects" + return_type
rmd_scn_url = base_url + rmd_base_url + "/RMD_SCNs" + return_type

username = 'gfaulconbridge'
pswd = '654321'


def daily_cq_data():
    cca_def_data = []
    cca_scn_data = []
    rmd_def_data = []
    rmd_scn_data = []

    # CCA DEFs
    r = requests.get(cca_def_url, auth=(username, pswd))
    json_data = json.loads(r.text)
    for i in json_data['oslc_cm:results']:
        cca_def_data.append(defect_data_class.from_json(i))

    print("Num of CCA DEFs: ", len(cca_def_data))

    # RMD DEFs
    # r = requests.get(rmd_def_url, auth=(username, pswd))
    # json_data = json.loads(r.text)
    # for i in json_data['oslc_cm:results']:
        # rmd_def_data.append(defect_data_class.from_json(i))

    # print("Num of RMD DEFs: ", len(rmd_def_data))

    # CCA SCNs
    r = requests.get(cca_scn_url, auth=(username, pswd))
    json_data = json.loads(r.text)
    for i in json_data['oslc_cm:results']:
        cca_scn_data.append(scn_data_class.from_json(i))

    print("Num of CCA SCNs: ", len(cca_scn_data))

    # RMD SCNs
    # r = requests.get(rmd_scn_url, auth=(username, pswd))
    # json_data = json.loads(r.text)
    # for i in json_data['oslc_cm:results']:
        # rmd_scn_data.append(scn_data_class.from_json(i))

    # print("Num of RMD SCNs: ", len(rmd_scn_data))

    return cca_def_data, cca_scn_data, rmd_def_data, rmd_scn_data


def process_scn_data(scn_data):
    submitted = 0
    active = 0
    pending = 0
    validated = 0

    for item in scn_data:
        if ('Pending_SwMgr_Approval' in item.state or
            'Pending_LSE_Approval' in item.state or
            'Pending_LSwE_Approval' in item.state or
            'SCN_Created' in item.state):
            submitted += 1
        elif ('SW_Lifecycle' in item.state or
            'Developer_Tested' in item.state):
            active += 1
        elif ('Pending_Validation' in item.state):
            pending += 1
        elif ('Canceled' in item.state or
              'Confirmed_Superseded' in item.state or
              'Validated' in item.state):
            validated += 1
        else:
            print(item.state)

    print(active, pending, validated)
    return active, pending, validated


def process_def_data(def_data):
    submitted = 0
    active = 0
    pending = 0
    validated = 0

    for item in def_data:
        if ('Submitted' in item.state):
            submitted += 1
        elif ('Assigned' in item.state or
              'Opened' in item.state or
              'Developer_Tested' in item.state):
                active += 1
        elif ('Deleted' in item.state or
              'No_Problem' in item.state or
              'Pending_Validation' in item.state or
              'Unreproducable' in item.state):
            pending += 1
        elif ('Confirmed_No_Problem' in item.state or
              'Confirmed_Duplicate' in item.state or
              # 'Confirmed_Deferred' in item.state or
              'Confirmed_Unreproducible' in item.state or
              'Validated' in item.state):
            validated += 1
        # else:
            # print(item.state)

    print(active, pending, validated)
    return active, pending, validated

# cca_def_data, cca_scn_data, rmd_def_data, rmd_scn_data = daily_cq_data()
# process_def_data(cca_def_data)
# process_scn_data(cca_scn_data)
