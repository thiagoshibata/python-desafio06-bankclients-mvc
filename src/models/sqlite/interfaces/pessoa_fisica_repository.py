from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaInterface(ABC):

    @abstractmethod
    def list_pessoa_fisica(self) -> list[PessoaFisicaTable]:
        pass
