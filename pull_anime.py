#!/usr/bin/python
#This script will take your anime-planet.com username and scrape a list of your watched anime in XML utf-8 format to anime-planet.xml
 
from bs4 import BeautifulSoup,NavigableString
import urllib2,sys,re,codecs
 
print 'This script will export your anime-planet.com anime list and saves it to SpacePull.xml'
username = raw_input("Enter your username: ")
baseURL = 'http://www.anime-planet.com/users/'+username+'/anime'
html = urllib2.urlopen(baseURL).read()
html = BeautifulSoup(html)
pageNumber = int (html.find('li','next').findPrevious('li').next.contents[0])
delimiter = '\t'
 
f = codecs.open('spacePull.xml', 'w', 'utf-8')
 
print 'Exporting rough variant of Anime List format...'
for i in range(1,pageNumber+1):
        baseURL = 'http://www.anime-planet.com/users/'+username+'/anime?page='+str(i)
        html = urllib2.urlopen(baseURL).read()
        html = BeautifulSoup(html)
        for animeItem in html.findAll('tr')[1:]:
                animeItem = BeautifulSoup(animeItem.renderContents())
 
                f.write ('\t\t'+ animeItem.a.text +'\n');
                #f.write ('\t\t<update_on_import>1</update_on_import>\n');
 
print 'Done, see SpacePull.xml'
