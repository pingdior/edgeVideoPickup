from urlparse import urlparse
import urllib
import urllib2

url = 'https://vod.tencentcloudapi.com' 
values = {'Action' : 'WeChatMiniProgramPublish',
          'Version' : '2018-07-17',
          'FileId' : '5285890818826659013',
          'SourceDefinition':'0',
          'Timestamp':'888888888',
          'SubAppId':'1305387564'}
data = urllib.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib2.Request(url, data)
response = urllib2.urlopen(req) 
print response.read()

