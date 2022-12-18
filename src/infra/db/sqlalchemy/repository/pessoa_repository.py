from src.infra.db.sqlalchemy.entities import Pessoa

from src.infra.db.sqlalchemy.config import DBConnectionHandler

from typing import List,Optional

class PesssoaRepository():
    """Class to manage Pessoa Repository"""
    
    def add(self, pessoa: Pessoa) -> Pessoa:
        with DBConnectionHandler() as db_connection:
            try:
    
                db_connection.session.add(pessoa)
                db_connection.session.commit()
                db_connection.session.refresh(pessoa)

                return pessoa

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
    
    def list(self, limit: Optional[int] = 100, start: Optional[int] = 0) -> List[Pessoa]:
        with DBConnectionHandler() as db_connection:
            try:
                query = db_connection.session.query(Pessoa)

                res = query.offset(start).limit(limit).all()

                return res

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
    
    def delete(self, id: int) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                db_connection.session.query(Pessoa).filter_by(id=id).delete()
                db_connection.session.commit()
                db_connection.session.flush()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        
    def edit(self, id: int, new_pessoa: Pessoa) -> Pessoa:
        with DBConnectionHandler() as db_connection:
            try:
                new_pessoa.id_pessoa = id
                updated_pessoa = db_connection.session.merge(new_pessoa)
                db_connection.session.commit()
                db_connection.session.refresh(updated_pessoa)

                return new_pessoa

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()