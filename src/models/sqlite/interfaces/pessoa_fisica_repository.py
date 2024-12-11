from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaInterface(ABC):

    @abstractmethod
    def list_pessoa_fisica(self) -> list[PessoaFisicaTable]:
        pass
    @abstractmethod
    def insert_pessoa_fisica(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        pass
