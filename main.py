from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
	data=[{'gen':'action'},{'gen':'romance'},{'gen':'sci-fi'},{'gen':'comedy'},{'gen':'horror'},{'gen':'thriller'},{'gen':'crime'},{'gen':'drama'},{'gen':'adventure'},{'gen':'fantasy'},{'gen':'animation'},{'gen':'superhero'},{'gen':'mystery'}]
	return(render_template('form.html',data=data))


@app.route("/scrap",methods=['GET','POST'])	
def scraper():
	genre=request.form.get('genre')
	url="https://www.imdb.com/search/title?title_type=feature&genres="+genre+"&languages=en&sort=user_rating,desc"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	x=soup.find_all('div',class_="lister-item mode-advanced")
	result=[]
	for res in x[:5]:
		result+=[res.h3.a.get_text()]
	print(genre)
	return(render_template('scrap.html',result=result,genre=genre))


if(__name__=="__main__"):
	app.run(debug=True)