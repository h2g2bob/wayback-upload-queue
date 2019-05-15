#!/usr/bin/env python3
import requests
from csv import DictReader
from io import StringIO

CANDIDATE_URL='https://candidates.democracyclub.org.uk/media/candidates-europarl.2019-05-23.csv'

def download_data():
    req = requests.get(CANDIDATE_URL)

    # avoid: "_csv.Error: new-line character seen in unquoted field - do you
    # need to open the file in universal-newline mode?"
    stream = StringIO(req.text, newline='')

    csvdata = DictReader(stream)
    return csvdata

def main():
    for row in download_data():
        for col in row.values():
            if col.startswith("http://") or col.startswith("https://"):
                print(col)

if __name__ == '__main__':
    main()

