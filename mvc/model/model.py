import mysql.connector

class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='user_alumnos', 
                password='1234',
                host='127.0.0.1',
                port=3306,
                database='escuela',
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print("el error es:"+str(e))

    def select(self):
        try:
            self.connect()
            query = ("SELECT * from alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id_persona':row[0],
                    'nombre':row[1],
                    'ap_uno': row[2],
                    'ap_dos': row[3],
                    'matricula': row[4],
                    'edad': row[5],
                    'genero': row[6],
                    'estado_civil': row[7],
                    'fec_nac': row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result
    
    def view(self,id_persona):
        try:
            self.connect()
            query = ("SELECT * from alumnos where id_persona = %s;")
            values = (id_persona,)
            self.cursor.execute(query,values)
            result = []
           
            for row in self.cursor:
                r = {
                    'id_persona':row[0],
                    'nombre':row[1],
                    'ap_uno': row[2],
                    'ap_dos': row[3],
                    'matricula': row[4],
                    'edad': row[5],
                    'genero': row[6],
                    'estado_civil': row[7],
                    'fec_nac': row[8]
                }
                result.append(r)
            if(len(result)==0):
                result=self.select()
                print("eso es select")
                print(result)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    def insert(self, nombre, ap_uno,ap_dos,matricula,edad,genero,estado_civil,fec_nac):
        try:
            self.connect()
            query = ("INSERT INTO alumnos (nombre,ap_uno,ap_dos,matricula,edad,genero,estado_civil,fec_nac) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (nombre, ap_uno,ap_dos,matricula,edad,genero,estado_civil,fec_nac)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def update(self,id_persona, campo,valor):
        try:
            print(id_persona)
            print(campo)
            print(valor)
            self.connect()
            query = ("update alumnos set "+str(campo)+"= '"+str(valor)+"' where id_persona="+str(id_persona)+";")
            print(query)
            #values = (campo,valor,id_persona)
            self.cursor.execute(query)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def delete(self, id_persona):
        try:
            self.connect()
            query = ("delete from alumnos WHERE id_persona ="+str(id_persona)+";")
            values = (id_persona)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Alumnos()


"""
    
        """


