#-*- coding: utf-8 -*-

#Consultation API news avec NewsAPI

import requests
import json
import webbrowser

#API key = b6ebf2a8daf84277981eb42ab04c48f9

#donne à l'utilisateur les différents médias auquel il peut avoir accès
url_sources = "https://newsapi.org/v1/sources"
r_sources = requests.get(url_sources)
data_sources = r_sources.json()
ressources = raw_input("Voulez vous connaitre les differents medias disponibles ? ")
if "oui" in ressources:
	#print(data_sources)
	for i in range(70):
		nom = data_sources['sources'][i]['name']
		print(nom)
		
#Bizarre ça ne marche pas avec tous les médias, certains sont non existants et d'autre ont des soucis d'affichage

#choix du média dont l'utilisateur veut connaitre les articles
sites_news = raw_input("De quel media voulez vous lire les articles ? ")
url_articles = "https://newsapi.org/v1/articles?source="+sites_news+"&sortBy=latest&apiKey=b6ebf2a8daf84277981eb42ab04c48f9"
r_articles = requests.get(url_articles)
data_articles = r_articles.json()
#print(data_articles)

#récupération des données des articles (titre, auteur...) et stockage des urls dans une liste
liste_urls = []
for i in range (0,10):
	titre = data_articles['articles'][i]['title']
	auteur = data_articles['articles'][i]['author']
	date = data_articles['articles'][i]['publishedAt']
	url = data_articles['articles'][i]['url']
	articles = titre + " par " + auteur + " le " + date + "\n" + "url : " + url
	print(articles)
	liste_urls.append(url)

#print(liste_articles)
taille_liste = len(liste_urls)

#demande si l'utilisateur veut avoir accès à un des articles
lecture = raw_input("Voulez vous que je vous lise un de ces articles ? ")
if "oui" in lecture:
	choix_article = input("Quel article voulez vous ? ")
	
	#ouvre la page web correspondant à l'article de notre choix
	for i in range(taille_liste):
		if i == choix_article:
			print("ok je vais ouvrir la page web")
			webbrowser.open(liste_urls[i])
