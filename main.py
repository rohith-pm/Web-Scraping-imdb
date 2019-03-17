from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
	data=[{'gen':'action'},{'gen':'romance'},{'gen':'sci-fi'},{'gen':'comedy'},{'gen':'horror'},{'gen':'thriller'},{'gen':'crime'},{'gen':'drama'},{'gen':'adventure'},{'gen':'fantasy'},{'gen':'animation'},{'gen':'superhero'},{'gen':'mystery'}]
	language=[{'lang':'english'},{'lang':'hindi'},{'lang':'tamil'},{'lang':'telugu'}]
	return(render_template('form.html',data=data,language=language))


@app.route("/scrap",methods=['GET','POST'])	
def scraper():
	genre=request.form.get('genre') #get genre
	language=request.form.get('language') #get language
	lang=language
	if(language=='english'):
		language='en'
	elif(language=='hindi'):
		language='hi'
	elif(language=='tamil'):
		language='ta'
	else:
		language='te'
		
	#url according to selection
	url="https://www.imdb.com/search/title?title_type=feature&genres="+genre+"&languages="+language+"&sort=user_rating,desc"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	x=soup.find_all('div',class_="lister-item mode-advanced") #parent <div> for each movie
	result=[] #getting only 5 movies
	for res in x[:5]:
		result+=[res.h3.a.get_text()] #movie name present in anchor tag
		
	return(render_template('scrap.html',result=result,genre=genre,lang=lang))


if(__name__=="__main__"):
	app.run(debug=True)
