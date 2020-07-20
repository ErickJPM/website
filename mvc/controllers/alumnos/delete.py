import web
render = web.template.render('mvc/views/alumnos/')
import mvc.model.model as alumnos
model_alumnos= alumnos.Alumnos()
class Delete():
    def GET(self):
        result=model_alumnos.select()
        tam=len(result)
        return render.delete(result,tam)

    def POST(self):
        try:
            form=web.input()
            print(form)   
            model_alumnos.delete(int(form.borrar))
            result=model_alumnos.select()
            tam=len(result)
            return render.delete(result,tam)
        except Exception as error:
            return "Error" +str(error)