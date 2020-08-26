import cocktail_blender.database.settings as db_settings
import cocktail_blender.database.models as db_models

def initialize_database():
    db_models.Base.metadata.create_all(db_settings.engine)


def reset_database():
    db_models.Base.metadata.drop_all(db_settings.engine)
    initialize_database()
