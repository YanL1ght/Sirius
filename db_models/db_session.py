import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session


SqlAlchemyBase = orm.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file:
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import db_reviews, db_places

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
