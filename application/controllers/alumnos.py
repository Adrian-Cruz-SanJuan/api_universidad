import web
import app
import json
render=web.template.render('application/views/')

class Alumnos:
    def GET(self):
        try:
            data=web.input()
            if data['action'] == 'get' and data['token'] == '1234':
                matri='17161511'
                nombre='Dejha'
                first='Thoris'
                second='Barsoon'
                career='TI'
                
                result={}
                result['Matricula']=matri
                result['Nombre']=nombre
                result['Primer apellido']=first
                result['Second apellido']=second
                result['Carrera']=career
                result['status']='200k'
                return json.dumps(result)
            else:
                result={}
                result['status']='token mal'
                return json.dumps(result)
        
        except Exception as e:    
            result['status']='error'
            return json.dumps(result)
   
