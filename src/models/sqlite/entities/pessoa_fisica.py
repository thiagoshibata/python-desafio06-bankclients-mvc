from sqlalchemy import Column, String, REAL, BIGINT
from src.models.sqlite.settings.base import Base

class PessoaFisicaTable(Base):
    __tablename__ = "pessoa_fisica"
    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_completo = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"pessoa_fisica [renda_mensal={self.renda_mensal}, idade={self.idade}, nome_completo={self.nome_completo}, celular={self.celular}, email={self.email}, categoria={self.categoria}, saldo={self.saldo}, id={self.id}]"
