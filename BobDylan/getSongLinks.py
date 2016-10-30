import urllib
import time

testfile = urllib.URLopener()

link = "http://www.songlyrics.com/bob-dylan-lyrics"
filename = "mainPage.txt"

testfile.retrieve(link, filename)

file = open("mainPage.txt", "r")
data = file.read()

beginning_tag = '<td width="93%"><a href="'
newdata = data.split(beginning_tag)[1:]
#print newdata

end_tag = '/"'

song_links = []
links = open("dylanLinks.txt", "w")
for s in newdata:
	link = s.split(end_tag)[0]
	song_links.append(link)
	links.write(link + "\n")
