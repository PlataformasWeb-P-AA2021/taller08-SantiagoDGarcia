from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

jugador = session.query(Jugador).order_by(Jugador.altura).all()

for x in jugador: 
    print(x) 