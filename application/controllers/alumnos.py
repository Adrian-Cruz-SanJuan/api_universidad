import web
import app
import json
import csv

render = web.template.render('application/controllers/')   #En esta no se ocupa

class Alumnos:
    def GET(self):
        try:
            datos=web.input()     #Los datos introducidos por el usuario se almacenaran en datos
            if datos['token']=="1234":     #Si el usuario ingresa bien el token se declarara lo siguiente
                result=[]           #Un arreglo
                result2={}          #Un diccionario
                if datos['action']=="get":        #Si accion es get va a hacer lo siguiente
                    with open('static/csv/alumnos.csv','r') as csvfile:   #Ruta del archivo csv que va a leer, r es de lectura, csvfile es una variable cualquiera
                        reader = csv.DictReader(csvfile)         #Lector del archivo, DictReader te almacena los datos como en diccionario en este caso en la variable reader
                        for row in reader:              #Lee la primer fila y la manda la arreglo
                            result.append(row)          #Lo manda al arreglo result
                            result2['status']="200 OK"
                            result2['alumnos']=result      #Result2 en la posicion alumnos, sera lo que va a almacenar en result
                    return json.dumps(result2)          #Va a regresar un json del result2 que es lo que va almacenando el arreglo
                else:                           #Si accion no es get va a poner comando no encontrado
                    result2={}
                    result2['status']="Command not found"
                    return json.dumps(result2)
            else:
                result={}
                result['status']="Los datos insertados son incorrectos"
                return json.dumps(result)
        except Exception:
            result={}
            result['status']="Faltan valores por insertar"
            return json.dumps(result)