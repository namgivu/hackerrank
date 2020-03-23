from src.mkdir_json import make_path


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


    def test1(self):  #TODO this fails why?
        d = {}
        d = make_path(d, 'path-to', 'my', 'keys')
        assert d.get('path-to') is not None

        '''
        TODO this test failed pls fix
        
        def test0(self):
            d = {}
            d = make_path(d, 'path-to', 'my', 'keys')
        >       assert d.get('path-to') is not None
        E       AssertionError: assert None is not None
        E        +  where None = <built-in method get of dict object at 0x7f3ad5109140>('path-to')
        E        +    where <built-in method get of dict object at 0x7f3ad5109140> = {}.get
        tests/test_mkdir_json.py:9: AssertionError
        '''
