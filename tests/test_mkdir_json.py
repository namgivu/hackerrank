from src.mkdir_json import make_path, mkdir_json


class Test:

    #region test0 related

    def test0(self):
        d = {}
        make_path(d, 'path-to', 'my', 'keys')['test'] = 122
        assert d['path-to']['my']['keys']['test'] == 122


    def test0b(self):  #NOTE this will fail; see resolution in test0c()
        d = {}
        d = make_path(d, 'path-to', 'my', 'keys')
        d['path-to']['my']['keys']['test'] = 122
        assert d['path-to']['my']['keys']['test'] == 122


    def test0c(self):
        """same as test0b but d not get from d= make_path()"""
        d = {}
        make_path(d, 'path-to', 'my', 'keys')
        d['path-to']['my']['keys']['test'] = 122
        assert d['path-to']['my']['keys']['test'] == 122


    def test0d(self):
        d = {}

        make_path(d, 'path-to', 'my', 'keys')
        assert d['path-to']               is not None
        assert d['path-to']['my']         is not None
        assert d['path-to']['my']['keys'] is not None

        d['path-to']['my']['keys']['test'] = 122
        assert d['path-to']               is not None
        assert d['path-to']['my']         is not None
        assert d['path-to']['my']['keys'] is not None
        assert d['path-to']['my']['keys']['test'] == 122

    #endregion test0 related


    def test1(self):  #NOTE this will fail
        d = {}
        d = make_path(d, 'path-to', 'my', 'keys')
        assert d.get('path-to') is not None  # Failed because make_path()


class Test_mkdir_json:
    def test__mkdir_json(self):
        d = {}

        mkdir_json(d, 'path-to', 'my', 'keys')
        assert d['path-to']               is not None
        assert d['path-to']['my']         is not None
        assert d['path-to']['my']['keys'] is not None

        d['path-to']['my']['keys']['test'] = 122
        assert d['path-to']['my']['keys']['test'] == 122
