try:
    assert 1==2, 'Some error 22'

except AssertionError as e:
    from pprint import pprint
    pprint(e)
    print(e)
    print(type(e))
    print(str(e))

    #can cast Exception to falcon.HTTPBadRequest() here ref. https://stackoverflow.com/a/1569074/248616
    #e.g.
    #raise falcon.HTTPBadRequest(e)
