from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository

db_connection_handler.connect_to_db()

def test_list_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.list_pessoa_fisica()
    print()
    print(response)

def test_list_pessoa_juridica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.list_pessoa_juridica()
    print()
    print(response)
