from typing import List, Dict
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaInterface
from src.controllers.interfaces.pessoa_fisica_lister_controller import PessoaFisicaListerControllerInterface

class PessoaFisicaListerController(PessoaFisicaListerControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def list(self) -> Dict:
        pessoas_fisicas = self.__get_pessoas_fisicas_in_db()
        response = self.__formated_response(pessoas_fisicas)
        return response

    def __get_pessoas_fisicas_in_db(self) -> List[PessoaFisicaTable]:
        pessoas_fisicas = self.__pessoa_fisica_repository.list_pessoa_fisica()
        return pessoas_fisicas

    def __formated_response(self, pessoas_fisicas: List[PessoaFisicaTable]) -> Dict:
        formated_pessoas_fisicas = []
        for pessoas_fisica in pessoas_fisicas:
            formated_pessoas_fisicas.append({
                "id": pessoas_fisica.id,
                "nome_completo": pessoas_fisica.nome_completo
            })

        return {
            "data": {
                "type": "Pessoas físicias",
                "count": len(formated_pessoas_fisicas),
                "attributes": formated_pessoas_fisicas
            }
        }
