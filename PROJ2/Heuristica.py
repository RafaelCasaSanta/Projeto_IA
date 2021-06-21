"""@static method
 def getHeuristica(caixas);
   for _ in range (10):
   caixas[_] = list( filter((0)).caixas[_])

   return len(caixa[0]) + len(caixas[1])""

""
"""
class Heuristica

tabuleiro = []
maxLength=0

caixarobo = []
paredes = []
movimentos_possiveis= {'B':[1,0] , 'C':[-1,0], 'D':[0,1], 'E'[0,-1] }

maxRowLength = 0	
lines=0

while(1): 
   line raw_input()
   if line!= "":
     lines +=1
     tabuleiro.append(line)
       if len(line)>maxRowLength:
			   maxRowLength=len(line)
         else:
           break

import time
time_start = time.clock()

for i in range(0,lines):
	caixarobo.append([])
	paredes.append([])
	for j in range(0,maxRowLength):
		caixarobo[-1].append('-')
		paredes[-1].append('-')

for i in range(0,len(tabuleiro)):
	if len(tabuleiro[i])<maxRowLength:
		for j in range(len(tabuleiro[i]),maxRowLength):
			tabuleiro[i]+='O'

for i in range(0,len(tabuleiro)):
	for j in range(0,maxRowLength):
		if tabuleiro[i][j]=='B' or tabuleiro[i][j]=='R':
			caixarobo[i][j]=tabuleiro[i][j]
			paredes[i][j]=' '
		elif tabuleiro[i][j]=='S' or tabuleiro[i][j]=='O':
			paredes[i][j] = tabuleiro[i][j]
			caixarobo[i][j] = ' '
		elif tabuleiro[i][j]==' ':
			caixarobo[i][j] = ' '
			paredes[i][j]=' '
		elif tabuleiro[i][j] == '*':
			caixarobo[i][j] = 'B'
			paredes[i][j] = 'S'
		elif tabuleiro[i][j] == '.':
			caixarobo[i][j] = 'R'
			paredes[i][j] = 'S'

storages = []
for i in range(0,lines):
	for j in range(0,maxRowLength):
		if paredes[i][j]=='S':
			storages.append([i,j])

print storages
distanciarobocaixa = 0
caixas=[]
storagesLeft = len(storages)
for i in range(0,lines):
	for j in range(0,maxRowLength):
		if boxRobot[i][j]=='B':
			if wallsStorageSpaces[i][j]=='S':
				print i,j
				storagesLeft-=1
			boxes.append([i,j])
print storagesLeft

