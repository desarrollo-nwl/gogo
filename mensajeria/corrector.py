# -*- encoding: utf-8 -*-
import string

def tildes(a_s):
	a_s = string.replace(a_s,'\xe1','&aacute;')
	a_s = string.replace(a_s,'\xe9','&eacute;')
	a_s = string.replace(a_s,'\xed','&iacute;')
	a_s = string.replace(a_s,'\xf3','&oacute;')
	a_s = string.replace(a_s,'\xfa','&uacute;')
	a_s = string.replace(a_s,'\xc1','&Aacute;')
	a_s = string.replace(a_s,'\xc9','&Eacute;')
	a_s = string.replace(a_s,'\xcd','&Iacute;')
	a_s = string.replace(a_s,'\xd3','&Oacute;')
	a_s = string.replace(a_s,'\xda','&Uacute;')
	a_s = string.replace(a_s,'\xf1','&ntilde;')
	a_s = string.replace(a_s,'\xd1','&Ntilde;')
	a_s = string.replace(a_s,'\xbf','&iquest;')
	a_s = string.replace(a_s,'\xa1','&iexcl;')
	a_s = string.replace(a_s,'\xdc','&Uuml;')
	a_s = string.replace(a_s,'\xfc','&uuml;')
	return a_s

def tildes2(a_s):
	import string
	a_s = string.replace(a_s,'\xe1','a')
	a_s = string.replace(a_s,'\xe9','e')
	a_s = string.replace(a_s,'\xed','i')
	a_s = string.replace(a_s,'\xf3','o')
	a_s = string.replace(a_s,'\xfa','u')
	a_s = string.replace(a_s,'\xc1','A')
	a_s = string.replace(a_s,'\xc9','E')
	a_s = string.replace(a_s,'\xcd','I')
	a_s = string.replace(a_s,'\xd3','O')
	a_s = string.replace(a_s,'\xda','U')
	a_s = string.replace(a_s,'\xf1','n')
	a_s = string.replace(a_s,'\xd1','N')
	a_s = string.replace(a_s,'\xbf','?')
	a_s = string.replace(a_s,'\xa1','!')
	a_s = string.replace(a_s,'\xdc','U')
	a_s = string.replace(a_s,'\xfc','u')
	return a_s
