# import json


class scn_data_class(object):
    submit_date = ''
    id_num = ''
    headline = ''
    state = ''
    sco_headline = ''
    submitter = ''
    assigned = ''
    assigned_validation = ''
    baseline_name = ''

    def __init__(self, val1, val2, val3, val4, val5, val6, val7, val8, val9=""):
        self.submit_date = val1
        self.id_num = val2
        self.headline = val3
        self.state = val4
        self.sco_headline = val5
        self.submitter = val6
        self.assigned = val7
        self.assigned_validation = val8
        self.baseline_name = val9

    def to_str(self):
        ret_str = str(self.submit_date) + " "
        ret_str += str(self.id_num) + " "
        ret_str += str(self.headline) + " "
        ret_str += str(self.state) + " "
        ret_str += str(self.sco_headline) + " "
        ret_str += str(self.submitter) + " "
        ret_str += str(self.assigned) + " "
        ret_str += str(self.assigned_validation) + " "
        ret_str += str(self.baseline_name) + " "

    @classmethod
    def from_json(cls, json_data):
        sub_date = ''
        id_num = ''
        headline = ''
        state = ''
        sco_headline = ''
        submitter = ''
        assigned = ''
        assigned_val = ''
        base_name = ''

        # print(json.dumps(json_data, indent=4, sort_keys=True))
        # print(json_data['id'], json_data['Headline'])

        if 'Submitted_date' in json_data.keys():
            sub_date = json_data['Submitted_date']

        if 'id' in json_data.keys():
            id_num = json_data['id']

        if 'SCN_Headline' in json_data.keys():
            headline = json_data['SCN_Headline']

        if 'State' in json_data.keys():
            state = json_data['State']

        if 'LSWE_SCO_Record' in json_data.keys():
            if(json_data['LSWE_SCO_Record'] is not '' and
               'oslc_cm:results' in json_data['LSWE_SCO_Record'].keys()):
                if(json_data['LSWE_SCO_Record']['oslc_cm:results'] is not '' and
                   'SCO_Headline' in json_data['LSWE_SCO_Record']['oslc_cm:results'][0].keys()):
                    sco_headline = json_data['LSWE_SCO_Record']['oslc_cm:results'][0]['SCO_Headline']

        if 'Requestor2' in json_data.keys():
            if(json_data['Requestor2'] is not '' and
               'oslc_cm:lable' in json_data['Requestor2'].keys()):
                submitter = json_data['Requestor2']['oslc_cm:label']

        if 'lswe_Sw_Eng_to_Assig' in json_data.keys():
            if(json_data['lswe_Sw_Eng_to_Assig'] is not '' and
               'dc:title' in json_data['lswe_Sw_Eng_to_Assig'].keys()):
                assigned = json_data['lswe_Sw_Eng_to_Assig']['dc:title']

        if 'Val_Engineer_Assig' in json_data.keys():
            if(json_data['Val_Engineer_Assig'] is not '' and
               'dc:title' in json_data['Val_Engineer_Assig'].keys()):
                assigned_val = json_data['Val_Engineer_Assig']['dc:title']

        if 'LC_SW_Baseline_Stateless' in json_data.keys():
            if(json_data['LC_SW_Baseline_Stateless'] is not '' and
               'dc:title' in json_data['LC_SW_Baseline_Stateless'].keys()):
                base_name = json_data['LC_SW_Baseline_Stateless']['dc:title']

        new_class = scn_data_class(
            sub_date,
            id_num,
            headline,
            state,
            sco_headline,
            submitter,
            assigned,
            assigned_val,
            base_name)

        return new_class
