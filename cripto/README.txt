Os seguintes ficheiros python foram usados:

1. decrypt.py - analisa o texto e verifica para possiveis tamanhos de chaves, 
se existem palavras do mesmo tamanho da chave iguais entre si a ocorrer nas frequencias correspondentes a multiplos de tamanho 
da chave.


2. decrypt2.py - uma variação do anterior, excepto que procura palavras iguais de varios tamanhos que possam estar contidos
nas frequencias correspondentes a multiplos de tamanho da chave.

3. frequencies.py - utilizado como auxiliar para decifrar o texto. analisa o texto para o tamanho da chave achado (8) e extrai as 5 letras mais ocorridas e 5 menos ocorridas em cada 
multiplo de posição de chave ao longo de todo o texto. Inclui um dicionario onde são mapeadas as palavras do alfabeto permutado ao alfabeto real.
O texto cifrado é decifrado de acordo com esse dicionario.