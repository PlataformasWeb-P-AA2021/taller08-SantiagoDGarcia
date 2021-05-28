from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Base = declarative_base()

class Jugador(Base):
    __tablename__ = 'jugadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    pais = Column(String(50), nullable=False)
    posicion = Column(String(50), nullable=False)
    numero = Column(Integer, nullable=False)
    nombre_FIFA = Column(String(50), nullable=False)
    nombre_camiseta = Column(String(50), nullable=False)
    goles = Column(Integer, nullable=False)
    caps = Column(Integer, nullable=False)
    altura = Column(Integer, nullable=False)

    def __repr__(self):
        return "Nombre:%s || Apellido:%s || Pais:%s || Posicion:%s || Numero:%s || Nombre FIFA:%s || Nombre camiseta:%s || Goles:%s || Caps:%s || Altura:%s ||\n"% (
                          self.nombre, 
                          self.apellido, 
                          self.pais,
                          self.posicion,
                          self.numero,
                          self.nombre_FIFA,
                          self.nombre_camiseta,
                          self.goles,
                          self.caps,
                          self.altura)



Base.metadata.create_all(engine)
