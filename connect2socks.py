import socks
from urlparse import urlparse
import os
 
#Extract proxy connection details from env variable
#proxy = urlparse(os.environ['QUOTAGUARDSTATIC_URL'])
 
s = socks.socksocket() 
#s.set_proxy(socks.SOCKS5, proxy.hostname, 8080, True, proxy.username,proxy.password)
s.set_proxy(socks.SOCKS5, "localhost", 8080)
host = "httpbin.org"
s.connect((host, 80))
request = "GET /ip HTTP/1.1\nHost: "+host+"\nUser-Agent:Mozilla 5.0\n\n"
s.send(request)
response = s.recv(1024)
print response
