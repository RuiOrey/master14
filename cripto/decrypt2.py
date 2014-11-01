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
text_file = open("repetitions.txt", "w")
for i in xrange(0,8):
	text_file.write("\nRange %d\n" % i )
	for x in xrange(3, 8):
		print "\n"
		print x 
		print ""
		a=list(chunkstring(tex[i:], x))
		lista_combinacoes.append(a)
		a2= list(set(a))
		#print a 
		#print a2
		for elemento in a2:
			if a.count(elemento)>2:
					lista_elementos_repetidos.append(elemento)
					print "\n"
					print elemento
					text_file.write("%s" % elemento )
					text_file.write(" %d\n" % a.count(elemento) )
					print a.count(elemento)			
					print "" 
		#print a
print lista_elementos_repetidos
text_file.close()
a=list(chunkstring(tex, 8))
dicionario = dict( [ (i, a.count(i)) for i in set(a) ] )
print dicionario
	
	

	
	
