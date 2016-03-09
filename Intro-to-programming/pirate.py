import urllib

text = "Hello friends, let us go to war. I hope we win this fight!"

connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text)
print connection.read()
connection.close()
