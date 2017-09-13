import urllib.request

url = urllib.request.urlopen("http://www.google.co.in/?gws_rd=ssl")
html = url.read()
print(html)
