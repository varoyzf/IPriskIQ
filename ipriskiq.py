import requests
import sys

# python ipriskiq.py <your_riskiq_username> <your_riskiq_token> file.txt

username = 'your@email.com'
key = 'your_riskiq_token'
auth = (username, key)
url = 'https://api.passivetotal.org/'
path_passive = 'v2/dns/passive'
path_classification = 'v2/actions/classification'
path_tags = 'v2/actions/tags'


def main_request(path, query):
    data = {"query": query}
    res = requests.get(url + path, auth=auth, json=data)
    return res.json()


with open(str(sys.argv[1])) as file:
    line = file.readline()
    while line:
        results = main_request(path_passive, line.strip())
        for i in results['results']:
            tags = main_request(path_tags, line.strip())
            classification = main_request(path_classification, line.strip())
            print('{} | Classification: "{}" | Tags: "{}" | Host: {}'.format(line.strip(),
                classification['classification'], tags['tags'], i['resolve']))
        # print('')
        line = file.readline()
