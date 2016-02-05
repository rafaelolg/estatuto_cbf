import urllib

for i in range(4, 67):
    url = "http://imguol.com/blogdojuca/1/files/2016/02/%d.jpg" % i
    file = "%d.jpg" %i
    urllib.urlretrieve (url,file)

