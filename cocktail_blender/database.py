from cocktail_blender.database_settings import engine


def initialize_database():
    from cocktail_blender.models import Base

    Base.metadata.create_all(engine)


def reset_database():
    from cocktail_blender.models import Base

    Base.metadata.drop_all(engine)
    initialize_database()
