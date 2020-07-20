import web
render = web.template.render('mvc/views/alumnos/')
import mvc.model.model as alumnos

model_alumnos= alumnos.Alumnos()

class List():
    
    def GET(self):
        result=model_alumnos.select()
        tam=len(result)
        print(tam)

        return render.list(result,tam)