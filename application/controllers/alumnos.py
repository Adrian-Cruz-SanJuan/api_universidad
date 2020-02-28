import web
import app
import json
import csv

render = web.template.render('application/controllers/')   #En esta no se ocupa

class Alumnos:
    def GET(self):
        #try:
        datos = web.input() 
        if datos['token']=="1234":
            result=[]
            result2={}
            if datos['action']=="get":
                with open('static/csv/alumnos.csv') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        result.append(row)
                        result2['status']="200 OK"
                        result2['appVersion']="1.0.1"
                        result2['alumnos']=result
                return json.dumps(result2)
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
            elif datos['action'] == "search":
                inf = {}
                inf['app_version']="0.2.0"
                inf['status']="200 OK"
                matricula = str(datos['matricula'])
                result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                with open('static/csv/alumnos.csv', 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    result=[]
                    for row in reader:
                        if row[0]==matricula:
                            resulta={}
                            resulta['matricula']=str(row['matricula'])
                            resulta['nombre']=str(row['nombre'])
                            resulta['primer_apellido']=str(row['primer_apellido'])
                            resulta['segundo_apellido']=str(row['segundo_apellido'])
                            resulta['carrera']=str(row['carrera'])
                            result.append(resulta)
                        inf['alumnos']=result
                return json.dumps(inf)
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
                print("Si se pudo burro")
            else:
                result2={}
                result2['status']="Command not found get"
                return json.dumps(result2)
        else:
            result={}
            result['status']="Los datos insertados son incorrectos"
            return json.dumps(result)
        """except Exception as e:
            result={}
            text= "ups algo paso{}".format(e.args)
            result  ['status'] = text 
            return json.dumps(result)"""