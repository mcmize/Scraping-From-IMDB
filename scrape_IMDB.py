import urllib
import urllib.request as uReq
site = "http://www.imdb.com/chart/tvmeter"
uClient = uReq.urlopen(site)
page_html = uClient.read()
uClient.close()

import bs4 
from bs4 import BeautifulSoup 

import pickle

soup = BeautifulSoup(page_html,"html.parser")

containers = soup.findAll("tbody",{"class":"lister-list"})
print(len(containers))    #1

print(type(containers[0]))

rows = containers[0].findAll("tr")

dataSet = {
	'Name Of Show':[],
	'Year Of Release':[],
	'Ranking Change_Jump':[],
	'Change':[],
	'Users_count':[],
	'Rating':[]

}

#print(rows[0].find("td",{"class":["ratingColumn","imdbRating"]}).text)
#print(str(int(rows[0].find("td",{"class":["ratingColumn","imdbRating"]}).find("strong")['title'].split()[3].replace(',',''))))
#print(type(rows[0].find("td",{"class":"titleColumn"}).find("a").text))
#print(rows[1].find("td",{"class":"titleColumn"}).find("span").text)
#print(rows[0].find("td",{"class":"titleColumn"}).find("div").findAll("span"))
#print(rows[5].find("td",{"class":"titleColumn"}).find("div").findAll("span")[1].attrs['class'][2])
#print(rows[4].find("td",{"class":"titleColumn"}).find("div").parent)
#print(rows[0].find("td",{"class":["ratingColumn","imdbRating"]}).text)


file = open("csvfile.csv","w+")

file.write('Name Of Show'+','+'Year Of Release'+','+'Ranking Change_Jump'+','+'Change'+','+'Users_count'+','+'Rating'+'\n')

for i in range(len(rows)):
	
	dataSet['Name Of Show'].append(rows[i].find("td",{"class":"titleColumn"}).find("a").text)


	dataSet['Year Of Release'].append(int(rows[i].find("td",{"class":"titleColumn"}).find("span").text.split('(')[1].split(')')[0]))
	
	if (rows[i].find("td",{"class":"titleColumn"}).find("div").text.split('(')[1].split(')')[0] == 'no change'):
		dataSet['Ranking Change_Jump'].append('0')
	else:
		dataSet['Ranking Change_Jump'].append(rows[i].find("td",{"class":"titleColumn"}).find("div").text.split('(')[1].split(')')[0].split('\n')[2].replace(',',''))
	
	if (rows[i].find("td",{"class":"titleColumn"}).find("div").find("span") == None):
		dataSet['Change'].append('no change')
	else:
		dataSet['Change'].append(rows[i].find("td",{"class":"titleColumn"}).find("div").findAll("span")[1].attrs['class'][2])	



	try :
		dataSet['Users_count'].append(str(int(rows[i].find("td",{"class":["ratingColumn","imdbRating"]}).find("strong")['title'].split()[3].replace(',',''))))
	except TypeError:
		dataSet['Users_count'].append("")
	
	dataSet['Rating'].append(rows[i].find("td",{"class":["ratingColumn","imdbRating"]}).text.split('\n')[1])

	file.write(str(dataSet['Name Of Show'][i])+","+str(dataSet['Year Of Release'][i])+","+str(dataSet['Ranking Change_Jump'][i])+","+str(dataSet['Change'][i])+","+str(dataSet['Users_count'][i])+","+str(dataSet['Rating'][i])+"\n")

file.close()	



	
'''
print(dataSet['Rating'])
print(dataSet['Name Of Show'])
print(dataSet['Year Of Release'])
print(dataSet['Ranking Change_Jump'])
print(dataSet['Change'])
'''





#print(rows[0].find("td",{"class":["ratingColumn","imdbRating"]}).text)
#print(str(int(rows[0].find("td",{"class":["ratingColumn","imdbRating"]}).find("strong")['title'].split()[3].replace(',',''))))
#print(type(rows[0].find("td",{"class":"titleColumn"}).find("a").text))
#print(rows[1].find("td",{"class":"titleColumn"}).find("span").text)
#print(rows[0].find("td",{"class":"titleColumn"}).find("div").findAll("span"))
#print(rows[5].find("td",{"class":"titleColumn"}).find("div").findAll("span")[1].attrs['class'][2])
#print(rows[4].find("td",{"class":"titleColumn"}).find("div").parent)
#print(rows[0].find("td",{"class":["ratingColumn","imdbRating"]}).text)


site = "http://www.imdb.com/chart/moviemeter"
uClient = uReq.urlopen(site)
page_html = uClient.read()
uClient.close()

soup = BeautifulSoup(page_html,"html.parser")

containers = soup.findAll("tbody",{"class":"lister-list"})
print(len(containers))    #1

print(type(containers[0]))

rows = containers[0].findAll("tr")

dataSet = {
	'Name Of Movie':[],
	'Year Of Release':[],
	'Ranking Change_Jump':[],
	'Change':[],
	'Users_count':[],
	'Rating':[]

}


file = open("csvfileMovies.csv","w+")

file.write('Name Of Movie'+','+'Year Of Release'+','+'Ranking Change_Jump'+','+'Change'+','+'Users_count'+','+'Rating'+'\n')

for i in range(len(rows)):
	
	dataSet['Name Of Movie'].append(rows[i].find("td",{"class":"titleColumn"}).find("a").text)


	dataSet['Year Of Release'].append(int(rows[i].find("td",{"class":"titleColumn"}).find("span").text.split('(')[1].split(')')[0]))
	
	if (rows[i].find("td",{"class":"titleColumn"}).find("div").text.split('(')[1].split(')')[0] == 'no change'):
		dataSet['Ranking Change_Jump'].append('0')
	else:
		dataSet['Ranking Change_Jump'].append(rows[i].find("td",{"class":"titleColumn"}).find("div").text.split('(')[1].split(')')[0].split('\n')[2].replace(',',''))
	
	if (rows[i].find("td",{"class":"titleColumn"}).find("div").find("span") == None):
		dataSet['Change'].append('no change')
	else:
		dataSet['Change'].append(rows[i].find("td",{"class":"titleColumn"}).find("div").findAll("span")[1].attrs['class'][2])	



	try :
		dataSet['Users_count'].append(str(int(rows[i].find("td",{"class":["ratingColumn","imdbRating"]}).find("strong")['title'].split()[3].replace(',',''))))
	except TypeError:
		dataSet['Users_count'].append("")
	
	dataSet['Rating'].append(rows[i].find("td",{"class":["ratingColumn","imdbRating"]}).text.split('\n')[1])

	file.write(str(dataSet['Name Of Movie'][i])+","+str(dataSet['Year Of Release'][i])+","+str(dataSet['Ranking Change_Jump'][i])+","+str(dataSet['Change'][i])+","+str(dataSet['Users_count'][i])+","+str(dataSet['Rating'][i])+"\n")

file.close()