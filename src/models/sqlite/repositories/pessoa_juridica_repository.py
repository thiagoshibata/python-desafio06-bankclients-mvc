from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable

class PessoaJuridicaRepository():
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def insert_pessoa_juridica(self):
        pass

    def list_pessoa_juridica(self) -> list[PessoaJuridicaTable]:
        with self.__db_connection as database:
            try:
                pessoas_juridicas = database.session.query(PessoaJuridicaTable).all()
                return pessoas_juridicas
            except NoResultFound:
                return []
