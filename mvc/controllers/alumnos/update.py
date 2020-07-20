import web
render = web.template.render('mvc/views/alumnos/')
import mvc.model.model as alumnos

model_alumnos= alumnos.Alumnos()
class Update():

    def GET(self):
        result=model_alumnos.select()
        tam=len(result)
        return render.update(result,tam)

    def POST(self):
        try:
            form=web.input()
            print("lleha,ps")
            print(form)
            result_search=model_alumnos.view(form.id)
            if(len(result_search)==1):
                if (form.campo=="nombre"):
                    model_alumnos.update(int(form.id),form.campo,form.name)
                elif(form.campo=="matricula"):
                    model_alumnos.update(int(form.id),form.campo,form.matricula)
                elif(form.campo=="ap_uno"):
                    model_alumnos.update(int(form.id),form.campo,form.apellido1)
                elif(form.campo=="ap_dos"):
                    model_alumnos.update(int(form.id),form.campo,form.apellido2)
                elif(form.campo=="edad"):
                    model_alumnos.update(int(form.id),form.campo,form.age)
                elif(form.campo=="fec_nac"):
                    model_alumnos.update(int(form.id),form.campo,form.Nacimiento)
                elif(form.campo=="sexo"):
                    model_alumnos.update(int(form.id),form.campo,form.genero)
                elif(form.campo=="estado_civil"):
                    model_alumnos.update(int(form.id),form.campo,form.estado)
            result=model_alumnos.select()
            tam=len(result)
            return render.update(result,tam)



        except Exception as error:
            return "Error" +str(error)