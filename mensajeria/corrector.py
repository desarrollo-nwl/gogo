# -*- encoding: utf-8 -*-
import string

def salvar_html(a):
	a = string.replace(a,'&lt;','<')
	a = string.replace(a,'&gt;','>')
	a = string.replace(a,'&equals;','=')
	a = string.replace(a,'&semi;',';')
	a = string.replace(a,'&semi;',';')
	a = string.replace(a,'&colon;',':')
	a = string.replace(a,'&percnt;','%%')
	a = string.replace(a,'&commat;','@')
	a = string.replace(a,'&nbsp;',' ')
	a = string.replace(a,'&amp;','&')
	return a
