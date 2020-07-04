import os
import atexit

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import NullPool

import cocktail_blender.configuration as config

COCKTAILBLENDER_HOME = None
SQL_ALCHEMY_CONN = None

engine = None
Session = None


def configure_vars():
    global COCKTAILBLENDER_HOME
    global SQL_ALCHEMY_CONN
    COCKTAILBLENDER_HOME = os.path.expanduser(os.path.expandvars(config.get('COCKTAILBLENDER_HOME')))
    SQL_ALCHEMY_CONN = 'sqlite:///{}/cocktailblender.db'.format(COCKTAILBLENDER_HOME)


def configure_orm():
    global engine
    global Session

    engine_args = {"poolclass": NullPool}
    engine = create_engine(SQL_ALCHEMY_CONN, **engine_args)
    Session = scoped_session(
        sessionmaker(
            autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
        )
    )


def dispose_orm():
    global engine
    global Session

    if Session is not None:
        Session.remove()
        Session = None
    if engine is not None:
        engine.dispose()
        engine = None


configure_vars()
configure_orm()
atexit.register(dispose_orm)
