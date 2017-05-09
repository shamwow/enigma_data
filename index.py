import csv
from datetime import datetime

def check_id(id, row):
    try:
        int(id)
    except ValueError:
        print 'primaryid not a valid integer on row #%s' % row

def check_drug_name(name, row):
    if len(name) == 0:
        print 'drug_name is blank on row #%s' % row
    elif name.upper() != name:
        print 'drug_name is not uppercase on row %s' % row

def check_validated_verbatim_drugname(validated_name, row):
    try:
        parsed = int(validated_name)
    except ValueError:
        print 'validated_verbatim_drugname not a valid integer on row #%s' % row

def check_dose_verbatim(dose_verbatim, row):
    pass

def check_patient_gender(gender, row):
    if gender != 'M' and gender != 'F' and len(gender) != 0:
        print 'patient_gender not M, F, nor blank on row #%s' % row

def check_patient_weight(weight, row):
    try:
        parsed = float(weight)
    except ValueError:
        print 'patient_weight not a valid integer on row #%s' % row

def check_weight_unit(weight, unit, row):
    if weight == '0' and len(unit) != 0:
        print 'weight is 0 but weight_unit is not blank on row #%s' % row
    elif weight != '0' and (unit != 'KG' and unit != 'LBS'):
        print 'weight_unit is not LBS nor KG on row #%s' % row

def check_report_date(date, row):
    try:
        datetime.strptime(date, '%Y%M%d')
        if len(date) < 8:
            raise ValueError
    except ValueError:
        try:
            datetime.strptime(date, '%Y-%M-%d')
        except ValueError:
            print 'report_date not formated as YYYYMMdd or YYYY-MM-dd on row #%s' % row


with open('bad_data.csv', 'rb') as file:
    bad_data = csv.reader(file, delimiter=',', quotechar='"')
    for idx, row in enumerate(bad_data):
        # Skip column titles.
        if idx == 0:
            continue

        if len(row) > 8:
            print 'More than 8 columns on row #%s' % idx
            continue
        elif len(row) < 8:
            print 'Less than 8 columns on row #%s' % idx
            continue

        row = map(lambda x: x.strip(), row)

        check_id(row[0], idx)
        check_drug_name(row[1], idx)
        check_validated_verbatim_drugname(row[2], idx)
        check_dose_verbatim(row[3], idx)
        check_patient_gender(row[4], idx)
        check_patient_weight(row[5], idx)
        check_weight_unit(row[5], row[6], idx)
        check_report_date(row[7], idx)


