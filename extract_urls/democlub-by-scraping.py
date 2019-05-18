#!/usr/bin/env python3
import re
import requests
from csv import DictReader
from io import StringIO

CANDIDATE_URL='https://candidates.democracyclub.org.uk/media/candidates-europarl.2019-05-23.csv'
HTTP_REGEX=re.compile(r'[\"\'\s](https?://[^\s\"\'<>]+)[\"\'\s]')

def download_csv_data():
    req = requests.get(CANDIDATE_URL)

    # avoid: "_csv.Error: new-line character seen in unquoted field - do you
    # need to open the file in universal-newline mode?"
    stream = StringIO(req.text, newline='')

    csvdata = DictReader(stream)
    return csvdata

def download_candidate_ids():
    return [int(row['id']) for row in download_csv_data()]

def download_page(candidate_id):
    url = 'https://candidates.democracyclub.org.uk/person/{}/'.format(candidate_id)
    req = requests.get(url)
    return req.text

def main():
    for candidate_id in download_candidate_ids():
        page = download_page(candidate_id)
        for url in HTTP_REGEX.findall(page):
            print(url)

if __name__ == '__main__':
    main()

