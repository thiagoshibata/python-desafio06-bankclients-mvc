from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository

class PessoaFisicaCreateController:
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepository):
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def create(self, pessoa_fisica_info: dict) -> dict:
        renda_mensal = pessoa_fisica_info["renda_mensal"]
        idade = pessoa_fisica_info["idade"]
        nome_completo = pessoa_fisica_info["nome_completo"]
        celular = pessoa_fisica_info["celular"]
        email = pessoa_fisica_info["email"]
        categoria = pessoa_fisica_info["categoria"]
        saldo = pessoa_fisica_info["saldo"]

        # inserir método de validação do nome

        self.__insert_pessoa_fisica_in_db(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        formated_response = self.__format_response(pessoa_fisica_info)
        return formated_response

    def __insert_pessoa_fisica_in_db(self,renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.__pessoa_fisica_repository.insert_pessoa_fisica(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

    # def __validade_nome_completo(self):
        # pass

    def __format_response(self, pessoa_fisica_info: dict) -> dict:
        return {
            "data": {
                "type": "Pessoa física",
                "count": 1,
                "attributes": pessoa_fisica_info
            }
        }
