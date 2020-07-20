import web
render = web.template.render('mvc/views/alumnos/')
class Index():

    def GET(self):
        return render.index()