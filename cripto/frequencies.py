import string
def distanceLetters(a, b,abecedario):
	aValor=abecedario.index(a)
	bValor=abecedario.index(b)
	if bValor>aValor:
		return bValor-aValor
	return aValor-bValor
def inverterDicionario(map):
	inv_map = dict(
		(v, [k for (k, xx) in filter(lambda (key, value): value == v, map.items())]) 
		for v in set(map.values())
	)
	return inv_map
f=open('Output.txt','r')
texto =f.readline()
frequencia = 8
tamanho = len(texto)
numeroLetrasPermutacao=tamanho/frequencia
abc= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letras = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"a":0,"x":0,"y":0,"z":0}
frequencias = {"a":13.9, "b":1.0,"c": 4.4,"d":	5.4,"e": 12.2,"f": 1.0,"g":	1.2,"h": 0.8,"i": 6.9, "j":0.4, "k":0.1, "l":2.8, "m":4.2, "n":5.3,"o":	10.8,"p": 2.9, "q":0.9, "r":6.9,"s": 7.9, "t":4.9, "u":4.0, "v":1.3, "w":0.0, "x":0.3, "y":0.0, "z":0.4}
abcAll=[]
print "Test " + str(distanceLetters("d","b",abc))
print "\n\n\nFREQUENCY TOOL\n\n\n"
print "a to e: " + str(distanceLetters("a","e",abc)) + "\te to o: " + str(distanceLetters("o","e",abc)) + "\ta to o: " + str(distanceLetters("a","o",abc))  +"\n"
test=sorted(frequencias.items(), key=lambda x:x[1],reverse=True)
print test
for i in xrange(0,frequencia):
	abcAll.append(letras.copy())
for i in xrange(0,frequencia) :
	for j in xrange(0,numeroLetrasPermutacao-1):
		letra=texto[i+ j*frequencia]
		#print letra
		#print abcAll[i].get(letra)
		abcAll[i][letra]=abcAll[i].get(letra) + 1
for i in xrange(0,frequencia):
	linha ="\nCOL" + str(i+1)+":"
	test=sorted((abcAll[i]).items(), key=lambda x:x[1])
	size=len(test)
	for j in xrange(0,5):
		value = test[size-j-1] 
		frequency=round(0.0+ (float(value[1])/(float(numeroLetrasPermutacao))) *100.0,1)
		linha = linha +"\t"+ " " +value[0]+":"+ str(frequency) + ""
	linha = linha + "\t\t 5 lower:"
	for j in xrange(0,5):
		value = test[5-j] 
		frequency=round(0.0+ (float(value[1])/(float(numeroLetrasPermutacao))) *100.0,1)
		linha = linha +"\t"+ " " +value[0]+":"+ str(frequency) + ""
	print linha
correspondencias1 = {"a":"j", "b":"q","c": "y","d":	"v","e": "z","f": "e","g":	"d","h": "p","i": "x", "j":"h", "k":"u", "l":"f", "m":"c", "n":"r","o":	"i","p": "s", "q":"m", "r":"k","s": "n", "t":"l", "u":"g", "v":"b", "w":"a", "x":"o", "y":"t", "z":"w"}
correspondencias2 = {"a":"g", "b":"b","c": "a","d":	"o","e": "t","f": "w","g":	"j","h": "q","i": "y", "j":"v", "k":"z", "l":"e", "m":"d", "n":"p","o":	"x","p": "h", "q":"u", "r":"f","s": "c", "t":"r", "u":"i", "v":"s", "w":"m", "x":"k", "y":"n", "z":"l"}
correspondencias3 = {"a":"k", "b":"n","c": "l","d":	"g","e": "b","f": "a","g":	"o","h": "t","i": "w", "j":"j", "k":"q", "l":"y", "m":"v", "n":"z","o":	"e","p": "d", "q":"p", "r":"x","s": "h", "t":"u", "u":"f", "v":"c", "w":"r", "x":"i", "y":"s", "z":"m"}
correspondencias4 = {"a":"y", "b":"v","c": "z","d":	"e","e": "d","f": "p","g":	"x","h": "h","i": "u", "j":"f", "k":"c", "l":"r", "m":"i", "n":"s","o":	"m","p": "k", "q":"n", "r":"l","s": "g", "t":"b", "u":"a", "v":"o", "w":"t", "x":"w", "y":"j", "z":"q"}
correspondencias5 = {"a":"p", "b":"x","c": "h","d":	"u","e": "f","f": "c","g":	"r","h": "i","i": "s", "j":"m", "k":"k", "l":"n", "m":"l", "n":"g","o":	"b","p": "a", "q":"o", "r":"t","s": "w", "t":"j", "u":"q", "v":"y", "w":"v", "x":"z", "y":"e", "z":"d"}
correspondencias6 = {"a":"z", "b":"e","c": "d","d":	"p","e": "x","f": "h","g":	"u","h": "f","i": "c", "j":"r", "k":"i", "l":"s", "m":"m", "n":"k","o":	"n","p": "l", "q":"g", "r":"b","s": "a", "t":"o", "u":"t", "v":"w", "w":"j", "x":"q", "y":"y", "z":"v"}
correspondencias7 = {"a":"s", "b":"m","c": "k","d":	"n","e": "l","f": "g","g":	"b","h": "a","i": "o", "j":"t", "k":"w", "l":"j", "m":"q", "n":"y","o":	"v","p": "z", "q":"e", "r":"d","s": "p", "t":"x", "u":"h", "v":"u", "w":"f", "x":"c", "y":"r", "z":"i"}
correspondencias8 = {"a":"w", "b":"j","c": "q","d":	"y","e": "v","f": "z","g":	"e","h": "d","i": "p", "j":"x", "k":"h", "l":"u", "m":"f", "n":"c","o":	"r","p": "i", "q":"s", "r":"m","s": "k", "t":"n", "u":"l", "v":"g", "w":"b", "x":"a", "y":"o", "z":"t"}
lista_correspondencias=[inverterDicionario(correspondencias1),inverterDicionario(correspondencias2),inverterDicionario(correspondencias3),inverterDicionario(correspondencias4),inverterDicionario(correspondencias5),inverterDicionario(correspondencias6),inverterDicionario(correspondencias7),inverterDicionario(correspondencias8)]
linha2="1\t"
inha1="0\t"
for letra in correspondencias1:
    inha1 = inha1+letra
print inha1
for letra in correspondencias1:
    correspondencia= correspondencias1[letra]
    linha2 = linha2+correspondencia
print linha2
linha2="2\t"
for letra in correspondencias2:
    correspondencia= correspondencias2[letra]
    linha2 = linha2+correspondencia
print linha2
linha2="3\t"
for letra in correspondencias3:
    correspondencia= correspondencias3[letra]
    linha2 = linha2+correspondencia
print linha2
linha2="4\t"
for letra in correspondencias4:
    correspondencia= correspondencias4[letra]
    linha2 = linha2+correspondencia
print linha2
linha2="5\t"
for letra in correspondencias5:
    correspondencia= correspondencias5[letra]
    linha2 = linha2+correspondencia
print linha2
linha2="6\t"
for letra in correspondencias6:
    correspondencia= correspondencias6[letra]
    linha2 = linha2+correspondencia
print linha2
linha2="7\t"
for letra in correspondencias7:
    correspondencia= correspondencias7[letra]
    linha2 = linha2+correspondencia
print linha2
linha2="8\t"
for letra in correspondencias8:
    correspondencia= correspondencias8[letra]
    linha2 = linha2+correspondencia
print linha2
#print lista_correspondencias
textop=""
for i in xrange(0,tamanho):
	indice =i % 8
	if indice == 0:
		textop=textop+""
	if texto[i] in lista_correspondencias[indice]:
		letra=lista_correspondencias[indice][texto[i]]
	else:
		letra="_"
	#print letra
	textop=textop+str(letra[0])
print textop