import json
import requests

clientCrt = "<cert path>"
clientKey = "keys path"
base_addr = 'https://<Puppet server DNS>:8081'
url = f"{base_addr}/pdb/query/v4/nodes"
headers = {'content-type': 'application/json'}
r = requests.get(url, verify=False, 
                  headers=headers, cert=(clientCrt, clientKey))
for server in r.json():
    fact_url = f'{base_addr}/pdb/query/v4/facts'
    facts = requests.get(fact_url, data = {"certname" : server["certname"]}  ,verify=False, 
                  headers=headers, cert=(clientCrt, clientKey))
    print(facts.json())
