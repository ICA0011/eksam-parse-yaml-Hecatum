import yaml, requests
import urllib

url = 'http://upload.itcollege.ee/~aleksei/eksam.yaml'

def parse_yaml(url):
    
    ad = ''
    req = urllib.request.urlopen(url)
    yaml_obj = yaml.safe_load(req)

    for user in yaml_obj:
        for key, val in user.items():
            if val['permission'] == 'admin':
                ad = val['name']
    
    return ad



print(parse_yaml(url))