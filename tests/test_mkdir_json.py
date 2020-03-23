from src.mkdir_json import make_path


class Test:

    def test0(self):
        d = {}
        d = make_path(d, 'path-to', 'my', 'keys')
        assert d.get('path-to') is not None

    def test1(self):
        d = {}
        make_path(d, 'path-to', 'my', 'keys')['test'] = 122
        assert d['path-to']['my']['keys']['test'] == 122

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
