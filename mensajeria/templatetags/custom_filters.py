from django import template
import json

register = template.Library()

@register.filter
def jsonbr(value):
	x = json.loads(value)
	if x:
		html =''
		for i in x:
			html +=i+'<br>'
	else:
		html ='Ninguna seleccionada'
	return html

@register.filter
def jsonavg(value):
	x = json.loads(value)
	if x:
		html = sum(x)/len(x)
	else:
		html = 0
	return html

# @register.simpletag
# def saludar():
#	 return "Hola"
