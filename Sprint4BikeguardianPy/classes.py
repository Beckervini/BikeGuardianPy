
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column("nome", String(255), nullable=False)
    rg = Column("rg", Integer, nullable=False)
    genero = Column("genero", String(255), nullable=False)
    estd_civil = Column("estd_civil", String(255), nullable=False)
    escolaridade = Column("escolaridade", String(255), nullable=False)
    dt_emiss_rg = Column("dt_emiss_rg", String(255), nullable=False)
    uf = Column("uf", String(255), nullable=False)
    email = Column("email", String(255), nullable=False)
    data_nasc = Column("data_nasc", String(255), nullable=False)
    nacionalidade = Column("nacionalidade", String(255), nullable=False)
    telefone = Column("telefone", Integer, nullable=False)
    cpf = Column("cpf", Integer, unique=True, nullable=False)
    idade = Column("idade", Integer, nullable=False)
    endereco = Column("endereco", String(255), nullable=False)
    cep = Column("cep", Integer, nullable=False)
    bikes = relationship("Bike", back_populates="cliente")

    def exibir_detalhes(self):
        print("\nDetalhes do Cliente:")
        print("-" * 50)
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Estado Civil: {self.estd_civil}")
        print(f"Escolaridade: {self.escolaridade}")
        print(f"Gênero: {self.genero}")
        print(f"Idade: {self.idade}")
        print(f"RG: {self.rg}")
        print(f"Data emissão RG: {self.dt_emiss_rg}")
        print(f"Email: {self.email}")
        print(f"Data de nascimento: {self.data_nasc}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Telefone: {self.telefone}")
        print(f"CEP: {self.cep}")
    
        if getattr(self, 'bikes', None):  
            if len(self.bikes) > 0:
                print("\nBikes cadastradas:")
            for bike in self.bikes:
                print("-" * 50)
                print(f"Modelo: {bike.modelo}")
                print(f"Cor: {bike.cor}")
                print(f"Data da compra: {bike.data_compra}")
                print(f"Local da compra: {bike.local_compra}")
                print(f"Número de Série: {bike.numero_serie}")
                print(f"Preço: {bike.preco}")
                print(f"Revisão no último ano: {bike.revisao}")
                print(f"Acessórios da bike: {bike.acessorios}")
                print(f"Plano escolhido pelo cliente: {bike.plano}")
                print(f"Foto da frente: {bike.foto1}")
                print(f"Foto de trás: {bike.foto2}")
                print(f"Foto lado esquerdo: {bike.foto3}")
                print(f"Foto lado direito: {bike.foto4}")


class Bike(Base):
    __tablename__ = 'bikes'
    bike_id = Column(Integer, primary_key=True) 
    modelo = Column("modelo", String(255), nullable=False)
    marca = Column("marca", String(255), nullable=False)
    cor = Column("cor", String(255), nullable=False)
    data_compra = Column("data_compra", String(255), nullable=False)
    local_compra = Column("local_compra", String(255), nullable=False)
    numero_serie = Column("numero_serie", Integer, unique=True, nullable=False)
    preco = Column("preco", Float, nullable=False)
    revisao = Column("revisao", String(255), nullable=False)
    acessorios = Column("acessorios", String(255), nullable=False)
    plano = Column("plano", String(255), nullable=False)
    foto1 = Column("foto1", String(255), nullable=False)
    foto2 = Column("foto2", String(255), nullable=False)
    foto3 = Column("foto3", String(255), nullable=False)
    foto4 = Column("foto4", String(255), nullable=False)
    cliente_id = Column("cliente_id", Integer, ForeignKey('clientes.id'))
    cliente = relationship("Cliente", back_populates="bikes")
