import urllib
import time

import os

lyrics = open("lyrics.txt", "w")

for filename in os.listdir('/Users/annaevtushenko/Music'):
    f = open('/Users/annaevtushenko/Music/' + filename, "r")
    data = f.read()
    if data.find('<p id="songLyricsDiv"  class="songLyricsV14 iComment-text">') != -1:
    	newdata = data.split('<p id="songLyricsDiv"  class="songLyricsV14 iComment-text">')[1]
    	newdata2 = newdata.split('</p>')[0]
    	extra_string = '<img src="http://static.urx.io/units/web/urx-unit-loader.gif" style="display:none;" onload="var a=document.createElement(\'script\');a.setAttribute(\'src\',\'https://static.urx.io/units/web/728893b3-309e-424e-99c8-2213c9ddd1b0.min.js\'),this.parentNode.insertBefore(a,this);">'
    	newdata3 = newdata2.replace(extra_string, "")
    	newdata4 = newdata3.replace('<br />', '')
    	lyrics.write(newdata4 + "\n")

lyrics.close()