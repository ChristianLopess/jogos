import sys, os
from colorama import *

def clear():
 os.system('cls' if os.name=='nt' else 'clear')

def Scroll(contatual,texto):#CONFERE
  stop = contatual + 5
  for i in range(contatual,stop):
    print(texto[i].rstrip())
  return stop

def construirarv(texto):#CONFERE
  arvore = []
  cont1 = 0
  cont2 = 0
  for linhas in texto:
    linhas = linhas.split()
    for palavras in linhas:
      insertarvore(arvore, palavras, cont1, cont2)
      cont1 += 1
    cont2 += 1      
    cont1 = 0
  return arvore

def insertarvore(arvore, palavra, menor, maior):#CONFERE
  if len(arvore) == 0:
    arvore.append((palavra, [], [], []))
    arvore[0][1].append((menor,maior))
  elif palavra < arvore[0][0]:
    insertarvore(arvore[0][2], palavra, menor, maior)

  elif palavra > arvore[0][0]:
    insertarvore(arvore[0][3], palavra, menor, maior)

  elif palavra == arvore[0][0]:
    arvore[0][1].append((menor,maior))


def ArvFinder(arvore, palavra):#CONFERE
  if arvore[0][0] > palavra:
    if arvore[0][2] != []:
      encontrado = ArvFinder(arvore[0][2], palavra)
      return encontrado
    else:
      return False
  elif arvore[0][0] < palavra:
    if arvore[0][3] != []:
      encontrado = ArvFinder(arvore[0][3], palavra)
      return encontrado
    else:
      return False
  else:
    return arvore[0][1] 


def AcharPalavra(texto,palavra,pp,pa):
  parte1 = pp[pa][1] 
  parte2 = pp[pa][0]
  linhas = texto[parte1].split()
  contagem = len(linhas)
  for i in range(parte2):##ats
    print(linhas[i], end=" ")
  print(Fore.RED + linhas[parte2],end=" ")
  print(Style.RESET_ALL, end="")
  for i in range(parte2 + 1, contagem):##dps
    print(linhas[i], end=" ")
  if len(texto)-(parte1-1)>3:##rst
    print()
    for i in range(4):
      print(texto[parte1+(i+1)], end="")
  else:
    print()    
    for i in range(len(linhas)-(parte1-1)):
      print(texto[parte1+i], end="") 
  pa += 1
  print(Fore.RED + "\nOcorrência %s da palavra %s" % (pa, palavra))
  print(Style.RESET_ALL)


def main():			
  l = sys.argv
  l = ["visualtexto.py","texto.txt"]
  f = open(l[1],"r")
  completo = f.readlines()
  numerol = len(completo)
  arv = construirarv(completo)
  contatual = Scroll(0,completo)
  pala = "" 
  comando = ""  
  pp = False
  pa = 0


  while comando != "q":	
    comando = input(Fore.YELLOW + "\nInsira uma nova opção:")
    print(Style.RESET_ALL)
    clear()		
    if comando == "z":
        contatual = Scroll(contatual,completo)
        print(contatual)

    elif comando == "a":
        contatual -= 10
        contatual = Scroll(contatual,completo)
        print(contatual)

    elif comando == "f" or comando == "n":
      if comando == "f":
        pala = input(Fore.YELLOW + "Digite a palavra a ser encontrada:")
        print(Style.RESET_ALL)
        pa = 0 #posicao inicial
        pp = ArvFinder(arv, pala) #posicao palavra
      if pp!=False:
        AcharPalavra(completo,pala,pp,pa)
        if pa + 1 < len(pp):
          pa += 1
        else:
          pa = 0
      else:
        clear()
        Scroll(contatual-5,completo)
        print(Fore.RED + "\n0 ocorrências da palavra %s" % (pala))
        print(Style.RESET_ALL)

    elif comando == "n":
      clear()
      if pp != False:
        AcharPalavra(completo,pala,pp,pa)
        if pa + 1 < len(pp):
          pa += 1
        else:
          pa = 0
      else:
        clear()
        Scroll(contatual-5,completo)
        print(Fore.RED + "\n0 ocorrências da palavra %s" % (pala))
        print(Style.RESET_ALL)   
  f.close()        

if __name__ == '__main__':
	main()
			
