import os


def make_dirs(path):
    if not os.path.isdir(path):
        print('making')
        os.makedirs(path)


def get(key):
    if key.upper() == 'COCKTAILBLENDER_HOME':
        cocktailblender_home = os.environ.get('COCKTAILBLENDER_HOME')

        if cocktailblender_home is None:
            cocktailblender_home = '~/cocktailblender'

        cocktailblender_home = os.path.expanduser(os.path.expandvars(cocktailblender_home))
        make_dirs(cocktailblender_home)

        return cocktailblender_home
