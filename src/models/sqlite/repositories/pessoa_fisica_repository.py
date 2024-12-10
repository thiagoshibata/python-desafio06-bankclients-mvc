from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaRepository():
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def list_pessoa_fisica(self) -> list[PessoaFisicaTable]:
        with self.__db_connection as database:
            try:
                pessoas_fisicas = database.session.query(PessoaFisicaTable).all()
                return pessoas_fisicas
            except NoResultFound:
                return []
