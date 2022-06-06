import yaml, requests
import urllib

url = 'http://upload.itcollege.ee/~aleksei/eksam.yaml'

def parse_yaml(url):
    
    req = urllib.request.urlopen(url)
    yaml_obj = yaml.load(req)
    
    return req


print(parse_yaml(url))