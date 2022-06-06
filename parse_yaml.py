import yaml, requests
import urllib

url = 'http://upload.itcollege.ee/~aleksei/eksam.yaml'

def parse_yaml(url):
    
    req = urllib.request.urlopen(url)
    
    return req



x = urllib.request.urlopen(url)
print(x)