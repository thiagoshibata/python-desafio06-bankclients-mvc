from abc import ABC, abstractmethod
from typing import Dict

class PessoaFisicaListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
