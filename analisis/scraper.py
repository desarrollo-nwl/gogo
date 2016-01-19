# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
from collections import defaultdict
from django.db import models, transaction
from django.db.models import F
# from analisis.models import *
import collections,datetime, json, re, string, time, unicodedata, urllib2


def escoba(a):
	a = unicodedata.normalize('NFKD', a ).encode('ascii','ignore')
	a = str(a).lower()
	vector =['$',	'@',	'#',	',',	'(',	')',	'[',	']',
			'{',	'}',	"'",	'"',	'.',	'_',	':',	';',
			'+',	'-',	'*',	'/',	'=',	'?',	'&',	'%',
			'|',	'!',	'\n',	'~',	'^',	'`',	'\\',   '<',
			'>',]
	for i in vector:
		a = string.replace(a,i,'')
	return a

def norepeat(a):
	a = re.sub(r'([aeiou])\1+', r'\1', a)
	return a

def escoba2(a):
	limpio = []
	for j in a:
		if 'http' in j or 'twitter' in j or 'www' in j:
			j = 'htp'
		if 'jaja' in j or 'jeje' in j or 'jiji' in j or 'jojo' in j or 'juju' in j:
			j = 'jaja'
		j = norepeat(j)
		lenj = len(j)
		if lenj > 0 and lenj <=150:
			limpio.append(j)
	return limpio

Termino = escoba(u"ClaroColombia")
url_user = "https://twitter.com/search?q={0}&src=typd".format(Termino)
soup = BeautifulSoup(urllib2.urlopen(url_user).read(),"html.parser")
twitts = soup.find_all("p","TweetTextSize")
usuarios = soup.find_all("span","username js-action-profile-name")


def limpiar_urls(url,Termino):
	url = url.lower()
	vector = [
				"?","#",'twitter','about','login','account','help/verified',
				'/about','/tos','/privacy','/account','/begin_password_reset',
				'/login',Termino,'/search-advanced'
			 ]

	for i in vector:
		if i in url:
			return False

	return True

internos = []
for i in xrange(len(twitts)):
	if not Termino in usuarios[i].get_text().lower() :
		# print 'Usuario: ', usuarios[i].get_text().lower(),'\n Texto: ', twitts[i].get_text()
		internos.append( twitts[i].get_text() )



memoria = []
urla = soup.find_all("a")
for i in urla:
	try:
		if limpiar_urls(i['href'],Termino) and len(i['href']) > 1 and i['href'] not in memoria:
			# print i['href']
			memoria.append(i['href'])
	except:
		pass

externos = []

for i in memoria:

	if 'http' in i:
		soup = BeautifulSoup(urllib2.urlopen(i).read(),"html.parser")
		externos.append(soup.get_text())
	else:
		url_user = "https://twitter.com{0}".format(i)
		soup = BeautifulSoup(urllib2.urlopen(url_user).read(),"html.parser")
		twitts = soup.find_all("p","TweetTextSize")
		for i in twitts:
			internos.append( i.get_text() )

print externos
print internos

print collections.Counter(' '.join(internos))
