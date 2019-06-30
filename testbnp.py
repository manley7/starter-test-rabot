import urllib.request
contents = urllib.request.urlopen("https://bnpparibas-apiexplorer.openbankproject.com/?version=2.0.0&ignoredefcat=true#2_0_0-getCurrentUser").read()
print (contents)
