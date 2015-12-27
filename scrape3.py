import urllib2 
import requests
import os
import pandas as pd

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(wiki)
'''igdtuw="http://igdtuw.ac.in/" 
page1=urllib2.urlopen(igdtuw)'''

from BeautifulSoup import BeautifulSoup
soup=BeautifulSoup(page)
'''soup2=BeautifulSoup(page1)'''

print soup.prettify()
'''raw_input("Press enter to clear the screen")
os.system('clear')
print soup2.prettify()'''
print soup.title      #Return the content between opening and clsong including tag
#print soup.findAll("a")

'''all_links=soup.findAll("a")
for link in all_links :
	print link.get("href") '''


right_table=soup.find('table', { "class" : 'wikitable sortable plainrowheaders'})
print right_table

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for row in right_table.findAll("tr"):
	cells = row.findAll('td')
	states = row.findAll('th') #to store the second coloumn data
	if len(cells)==6:
                A.append(cells[0].find(text=True))
                B.append(states[0].find(text=True))
                C.append(cells[1].find(text=True))
                D.append(cells[2].find(text=True))
                E.append(cells[3].find(text=True))
                F.append(cells[4].find(text=True))
                G.append(cells[5].find(text=True))


df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G

raw_input("Press enter")
os.system('clear')
print df
