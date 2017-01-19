# import json


class defect_data_class(object):
    submit_date = ''
    id_num = ''
    headline = ''
    state = ''
    severity = ''
    assigned = ''
    submitter = ''
    version1 = ''
    version_fixed = ''
    version_validated = ''
    target_baseline_str = ''
    assigned_validation = ''
    baseline_name = ''

    def __init__(self, val1, val2, val3, val4, val5, val6, val7, val8, val9,
                 val10, val11, val12, val13):
        self.submit_date = val1
        self.id_num = val2
        self.headline = val3
        self.state = val4
        self.severity = val5
        self.assigned = val6
        self.submitter = val7
        self.version1 = val8
        self.version_fixed = val9
        self.version_validated = val10
        self.target_baseline_str = val11
        self.assigned_validation = val12
        self.baseline_name = val13

    def to_str(self):
        ret_str = str(self.submit_date) + " "
        ret_str += str(self.id_num) + " "
        ret_str += str(self.headline) + " "
        ret_str += str(self.state) + " "
        ret_str += str(self.severity) + " "
        ret_str += str(self.assigned) + " "
        ret_str += str(self.submitter) + " "
        ret_str += str(self.version1) + " "
        ret_str += str(self.version_fixed) + " "
        ret_str += str(self.version_validated) + " "
        ret_str += str(self.target_baseline_str) + " "
        ret_str += str(self.assigned_validation) + " "
        ret_str += str(self.baseline_name)
        return ret_str

    @classmethod
    def from_json(cls, json_data):
        sub_date = ''
        id_num = ''
        headline = ''
        state = ''
        severity = ''
        assigned = ''
        submitter = ''
        ver1 = ''
        ver_fix = ''
        ver_val = ''
        target_base = ''
        assigned_val = ''
        base_name = ''

        # print(json.dumps(json_data, indent=4, sort_keys=True))
        # print(json_data['id'], json_data['Assigned_to'])

        if 'Submit_Date' in json_data.keys():
            sub_date = json_data['Submit_Date']

        if 'id' in json_data.keys():
            id_num = json_data['id']

        if 'Headline' in json_data.keys():
            headline = json_data['Headline']

        if 'State' in json_data.keys():
            state = json_data['State']

        if 'Severity' in json_data.keys():
            severity = json_data['Severity']

        if 'Assigned_to' in json_data.keys():
            if json_data['Assigned_to'] is not '':
                assigned = json_data['Assigned_to']['dc:title']

        if 'Submitter' in json_data.keys():
            if 'dc:title' in json_data['Submitter'].keys():
                submitter = json_data['Submitter']['dc:title']
            elif 'oslc_cm:label' in json_data['Submitter'].keys():
                submitter = json_data['Submitter']['oslc_cm:label']

        if 'Version1' in json_data.keys():
            if json_data['Version1'] is not '':
                ver1 = json_data['Version1']

        if 'VersionFixed' in json_data.keys():
            if json_data['VersionFixed'] is not '':
                ver_fix = json_data['VersionFixed']

        if 'VersionValidated' in json_data.keys():
            if json_data['VersionValidated'] is not '':
                ver_val = json_data['VersionValidated']

        if 'Found_In_Baseline' in json_data.keys():
            if json_data['Found_In_Baseline'] is not '':
                target_base = json_data['Found_In_Baseline']['dc:title']

        if 'Validation_Assigned_To' in json_data.keys():
            assigned_val = json_data['Validation_Assigned_To']

        if 'Target_SW_Baseline2' in json_data.keys():
            if json_data['Target_SW_Baseline2'] is not '':
                base_name = json_data['Target_SW_Baseline2']['oslc_cm:label']

        new_class = defect_data_class(
                        sub_date,
                        id_num,
                        headline,
                        state,
                        severity,
                        assigned,
                        submitter,
                        ver1,
                        ver_fix,
                        ver_val,
                        target_base,
                        assigned_val,
                        base_name)

        return new_class
