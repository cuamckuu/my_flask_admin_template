import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    os.getenv("DATABASE_PATH"),
    echo=int(os.getenv("IS_SQLALCHEMY_ECHO")),
    convert_unicode=True,
    encoding="utf-8",
    connect_args={'timeout': 15}
)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import app.models

    Base.metadata.create_all(bind=engine)


def get_or_create(model, defaults=None, **kwargs):
    instance = db_session.query(model).filter_by(**kwargs).first()

    if instance:
        return instance, False

    else:
        kwargs.update(defaults or {})

        instance = model(**kwargs)
        db_session.add(instance)

        return instance, True
