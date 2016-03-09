import json
import urllib
response = urllib.urlopen('https://udacity.com/public-api/v0/courses')
json_response = json.loads(response.read())
for course in json_response['courses']:
    print course['title']
    print course['homepage']
