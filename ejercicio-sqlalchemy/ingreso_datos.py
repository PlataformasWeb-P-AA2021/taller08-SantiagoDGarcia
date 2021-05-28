from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Jugador
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Importacion de datos, clubs
archivo = open("data/mundial2018.csv", "r", encoding='utf-8')
lin = archivo.readlines()

data = list(map(lambda x: x.split("|"), lin))
data = list(filter(lambda x: x[0]!= "Numero", data))
limpia = list(map(lambda x: x[len(x)-1].replace("\n", ""), data))
var = 0
for x in data:
        session.add(Jugador(nombre=x[4], apellido=x[3], pais=x[2], posicion=x[6] ,numero=x[0], nombre_FIFA=x[1], nombre_camiseta=x[5], goles=limpia[var], caps=x[8] , altura=x[7] ) )
        var+=1
session.commit()