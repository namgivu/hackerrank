import unittest, os

def setUpModule():    pass   # nothing here for now
def tearDownModule(): pass   # nothing here for now


class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass   # nothing here for now
    def tearDown(self): pass   # nothing here for now


    def test(self):
        # ensure .env exists
        app_home = os.path.abspath(os.path.dirname(__file__) + '/..')  # ref. https://stackoverflow.com/a/3283326/248616
        env_exists = os.path.isfile(f'{app_home}/.env')
        if not env_exists: raise Exception(f'file not found .env - please clone one from {app_home}/.env-sample')

        # check .env keys
        DB_PORT = os.environ.get('DB_PORT')
        assert DB_PORT is not None
