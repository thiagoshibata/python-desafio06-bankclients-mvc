from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaRepository():
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def insert_pessoa_fisica(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica_data = PessoaFisicaTable(
                    renda_mensal=renda_mensal,
                    idade = idade,
                    nome_completo = nome_completo,
                    celular = celular,
                    email = email,
                    categoria = categoria,
                    saldo = saldo
                )
                database.session.add(pessoa_fisica_data)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception


    def list_pessoa_fisica(self) -> list[PessoaFisicaTable]:
        with self.__db_connection as database:
            try:
                pessoas_fisicas = database.session.query(PessoaFisicaTable).all()
                return pessoas_fisicas
            except NoResultFound:
                return []
