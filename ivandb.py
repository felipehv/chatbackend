import sqlite3
import datetime
import json as JSON

class DB():

    def __init__(self):
        self.conn = sqlite3.connect('ivan.db')


    def poblar(self):
        self.conn.execute("CREATE TABLE mensajes(origen, destino, mensaje, fecha)")
        self.conn.commit()
        self.conn.close()

    def nuevoMensaje(self, json):
        origen = json['origen']
        destino = json['destino']
        mensaje = json['mensaje']
        fecha = datetime.datetime.now()

        self.conn.execute("INSERT INTO mensajes VALUES(?,?,?,?)", (origen,destino,mensaje,fecha))
        self.conn.commit()
        self.conn.close()
        return JSON.dumps({"status": 1})

    def getMsgs(self, json):
        user = json["usuario"]
        fecha = json["fecha"]
        if fecha == None:
            a = self.conn.execute("SELECT mensaje, fecha FROM mensajes WHERE destino=?", (user,))
        else:
            a = self.conn.execute("SELECT mensaje, fecha FROM mensajes WHERE destino=? and fecha < ?", (user,fecha))
            
        ret = JSON.dumps({"status": 1, "mensajes": [x for x in a]})
        self.conn.close()
        return ret
if __name__ == "__main__":
    db = DB()
    db.poblar()