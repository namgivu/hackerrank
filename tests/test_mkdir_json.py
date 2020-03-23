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

    def test0(self):
        """testcase: the path has NO value"""
        d = {}

        mkdir_json(d, 'path-to', 'my', 'keys')
        assert d['path-to']               is not None
        assert d['path-to']['my']         is not None
        assert d['path-to']['my']['keys'] is not None

        d['path-to']['my']['keys']['test'] = 122
        assert d['path-to']['my']['keys']['test'] == 122


    def test1(self):
        """
        testcase: the path has values already
            init     path = l0.l1.l2_other has value set
            expected output to have l0.l1.l2_key default set
        """
        d             = {}
        d['l0']       = {}
        d['l0']['l1'] = {
            'l2_other': 'note that there is no :l1_key field here'
        }

        mkdir_json(d, 'l0', 'l1', 'l2_key')
        d['l0']['l1']['l2_key'] = 122
        assert d['l0']['l1']['l2_key'] == 122
        assert d['l0']['l1']['l2_other']
