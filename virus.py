import os
import pathlib
from random import randint

root = "C:/TESTAO"

#for que varre todas as pastas existentes dentro da pasta root
for path, subdirs, files in os.walk(root):

 print("Folder: " + path)
 print("Subfolders: " + str(subdirs))


 #For que roda por todos os arquivos no diretorio e os renomeia
 for name in files:

  #caso o nome selecionado seja igual a um nome ja usado
  try:

   #Muda a pasta local de trabalho para a pasta onde esta os subdiretorios (serve para os.getcwd() funcionar)
   os.chdir(path)

   #Printa o proximo arquivo a ser renomeado
   print("[FILE NAME] File to be renamed: " + name)

   #Salva o nome do arquivo a ser renomeado em filename e printa           
   filename = pathlib.PurePath(path, name)
   print("  old name is: " + str(pathlib.PurePath(path, name)))

   #Escolhe o novo nome, salva na variavel newname e printa
   newname = str(randint(0,9999999))
   print ("  new name is: " + os.getcwd() + '\\' + newname)

   #Renomeia o arquivo com nome filename com o nome newname
   os.rename(filename, pathlib.PurePath(path, newname))
   
  except:
   pass

 if len(subdirs) > 0:

  #for que roda por todos os subdiretorios do diretorio atual  
  for subnum in range(len(subdirs)):

   #Muda a pasta local de trabalho para a pasta onde esta os subdiretorios (serve para os.getcwd() funcionar)
   os.chdir(path)

   #Salva o nome da subdiretorio que sera renomeado em dirname e printa
   dirname = subdirs[subnum]
   print("[DIR NAME]dirname is " + dirname)

   #Escolhe um novo nome e salva na variavel newdirname
   newdirname = str(randint(0,9999999))
   #print ("  newdirname is: " + newdirname)

   #Renomeia o subdiretorio e printa. Parametros (path atual, path nova)
   os.rename(os.path.join(os.getcwd(), dirname),    os.path.join(os.path.abspath(os.path.join(os.path.abspath(subdirs[subnum]), os.pardir)) , newdirname))
   print("  old name is: " + os.path.join(os.getcwd(), dirname))
   print("  new name is: " + os.path.join(os.path.abspath(os.path.join(os.path.abspath(subdirs[subnum]), os.pardir)) , newdirname))

   #Atualiza o subnum com o novo nome
   subdirs[subnum] = newdirname
   

os.chdir(root)
