try:
    assert 1==2, 'Some error 22'
    print(1)
except Exception as e:
    from pprint import pprint
    pprint(e)
    print(e)
    print(type(e))
    print(str(e))
    print(22)

    #can cast Exception to falcon.HTTPBadRequest() here
