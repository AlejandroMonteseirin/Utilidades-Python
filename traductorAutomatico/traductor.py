from googletrans import Translator
import time
#pip3 install googletrans==3.1.0a0
#https://py-googletrans.readthedocs.io/en/latest/
def separar(archivoASeparar):
    valores=""
    keys=""
    with open(archivoASeparar,'r') as file:
        lines = file.read().split("\n")
    for line in lines:
        separado = line.split("=")
        valores=valores+separado[1]+"\n"
        keys=keys+separado[0]+"\n"



    textfile = open('valores.txt', 'w')
    textfile.write(valores)
    textfile.close()

    textfile = open('keys.txt', 'w')
    textfile.write(keys)
    textfile.close()


def juntar(keys,values):
    resultado=""
    
    with open(keys,'r') as file:
        with open(values,'r') as file2:

            keys = file.read().split("\n")
            valores = file2.read().split("\n")
            print(len(keys))
            print(len(valores))

            if(len(keys)!=len(valores)):
                print("No miden lo mismo")
                return ""
            indice=0
            for key in keys:
                if(len(key)>0):
                    resultado=resultado+key+"="+valores[indice]+"\n"
                    indice=indice+1
                else:
                    resultado=resultado+"//linea vacia**"
                    



    textfile = open('ptTraducido.txt', 'w')
    textfile.write(resultado)
    textfile.close()


def traducir(tipoTexto,origen,resultado):
    translator = Translator()
    translation = translator.translate("Prueba que funciona bien y los idiomas origen y destino son los adecuados",resultado,origen)
    
    print("traducciendo del "+translation.src +" al "+translation.dest)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")   
    print(translation)

    time.sleep(4)
    resultado=""
    with open('texto.txt','r') as file:
        lines = file.read().split("\n")
    indice=0
    for line in lines:
        separado = line.split("=")
        traduccion = translator.translate(separado[1],src=origen,dst=resultado)
        resultado=resultado+separado[0]+"="+traduccion.text+"\n"
        indice=indice+1
        print("traducido "+str(indice)+" de un total de "+str(len(lines)))
    textfile = open('traduccionautomatica.txt', 'w')
    textfile.write(resultado)
    textfile.close()



print("iniciando...\n")
#separar('texto.txt')
#juntar('keys.txt','pt.txt')
traducir("propierties","es","en")
print("\n FIN")