import web
import app
import json
import csv

render = web.template.render('application/controllers/')   #En esta no se ocupa

class Alumnos:
    def GET(self):
        datos = web.input() 
        if datos['token']=="1234":
            result=[]
            result2={}

            #Obtiene todo el contenido del archivo alumnos.csv
            if datos['action']=="get":
                with open('static/csv/alumnos.csv') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        result.append(row)
                        result2['status']="200 OK"
                        result2['appVersion']="1.0.1"
                        result2['alumnos']=result
                return json.dumps(result2)

            #Obtiene solo la fila que coincida el campo matricula
            elif datos['action']=="search":
                with open('static/csv/alumnos.csv','r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    result = []
                    for row in reader:
                        if str(row['matricula'])==datos['matricula']:
                            result.append(row)
                            result2['status']="200 OK"
                            result2['appVersion']="1.0.1"
                            result2['alumnos']=result
                return json.dumps(result2)

            #Inserta una nueva fila en el archivo alumnos.csv
            elif datos["action"] == "put":
                m1 = datos["matricula"]
                m2 = datos["nombre"]
                m3 = datos["primer_apellido"]
                m4 = datos["segundo_apellido"]
                m5 = datos["carrera"]
                result = []
                result.append(m1)
                result.append(m2)
                result.append(m3)
                result.append(m4)
                result.append(m5)
                with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                    writer = csv.writer(csvfiles)
                    writer.writerow(result)
                with open('static/csv/alumnos.csv') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        result.append(row)
                        result2['status']="200 OK"
                        result2['appVersion']="1.0.1"
                        result2['alumnos']=result
                return json.dumps(result2)

            #Elimina la fila completa donde coincida la matricula especificada        
            elif datos['action']=="delete":
                inf = {}
                inf['app_version']="0.2.0"
                inf['status']="200 OK"
                deleted = datos['matricula']
                with open('static/csv/alumnos.csv', 'r') as inp, open('static/csv/salida.csv', 'w') as out:
                    writer = csv.writer(out)
                    for row in csv.reader(inp):
                        if row[0] != deleted:
                            writer.writerow(row)
                            print(row)
                        elif row[0] == '':
                            continue
                with open('static/csv/salida.csv', 'r') as inp, open('static/csv/alumnos.csv', 'w') as out:
                    writer = csv.writer(out)
                    for row in csv.reader(inp):
                        writer.writerow(row)
                with open('static/csv/alumnos.csv') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        result.append(row)
                        result2['status']="200 OK"
                        result2['appVersion']="1.0.1"
                        result2['alumnos']=result
                return json.dumps(result2)  
                print("Si se pudo burro")

            #Este lo que hace es que se le da la columna que quiere que se le retorne
            #ejemplo: http://localhost:8080/alumnos?action=filter&filtro=matricula&token=1234
            #Esto da como resultado que solo se muestren las matriculas, y así con las demás columnas
            elif datos['action']=="filter":
                filtro = datos['filtro']
                with open('static/csv/alumnos.csv') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        result.append(row[filtro])
                        result2['status']="200 OK"
                        result2['appVersion']="1.0.1"
                        result2['alumnos']=result
                return json.dumps(result2)
            else:
                result2={}
                result2['status']="Command not found get"
                return json.dumps(result2)
        else:
            result={}
            result['status']="Los datos insertados son incorrectos"
            return json.dumps(result)