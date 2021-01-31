import json
import os
from zipfile import ZipFile


# Retrive Event Records from provided code_test.json.
with open('code_test.json') as f:
    records = json.load(f, parse_int=int)['Records']

filesToZip = []
# Loop for each record.
for record in records:
    # Declaring empty values for EventData.
    eventNameData = []
    eventFileName = ''
    for eventRecord in records:
        # For loop for records and match with Initial record loop.
        if eventRecord['eventName'] == record['eventName']:
            eventFileName = eventRecord['eventName'].lower() + '-event.json'
            eventNameData.append(eventRecord)

    # Check if folder exists..
    if not os.path.exists('jsonfiles'):
        os.makedirs('jsonfiles')
    # Write Event data to a Json file.
    with open('jsonfiles/' + eventFileName, 'w') as event_data_file:
        json.dump(eventNameData, event_data_file, indent=2)

    # Append FileName to Zip.
    filesToZip.append('jsonfiles/' + eventFileName)

# Sort records based on eventtime
sortedRecords = sorted(records,key=lambda x: x['eventTime'])

sortedFileName = 'jsonfiles/sorted-chronological.json'
with open(sortedFileName, 'w') as sorted_data_file:
        json.dump(sortedRecords, sorted_data_file, indent=2)

# Append Sorted Records Data Filename to Zip.
filesToZip.append(sortedFileName)

# writing json files to a zipfile
with ZipFile('jsonfiles.zip','w') as zip:
    # writing each file one by one
    for filesToZip in filesToZip:
        zip.write(filesToZip)