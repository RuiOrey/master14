import string
def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
	
f=open('cripto1initial.txt','r')
linha = f.readline()
tex = ''.join(string.split(linha))
lista_combinacoes =[]
lista_elementos_repetidos=[]

while (linha):
	linha = f.readline()
	tex = tex + ''.join(string.split(linha))
f.close()
print tex
text_file = open("Output.txt", "w")
text_file.write("%s" % tex)
text_file.close()
for x in xrange(4, 23):
	print "\n\n-------------------\n"
	print x 
	print "\n-------------------\n"
	a=list(chunkstring(tex, x))
	lista_combinacoes.append(a)
	a2= list(set(a))
	#print a 
	#print a2
	for elemento in a2:
		if a.count(elemento)>1:
				lista_elementos_repetidos.append(elemento)
				print "\n\n-------------------\n"
				print elemento
				print a.count(elemento)			
				print "\n-------------------\n" 
	#print a
print lista_elementos_repetidos

a=list(chunkstring(tex, 8))
dicionario = dict( [ (i, a.count(i)) for i in set(a) ] )
print dicionario
	
	

	
	
