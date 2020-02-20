from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web  # pip install web.py

urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
