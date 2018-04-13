try:
    assert 1==2, Exception('Some error 22')
    print(1)
except RuntimeError as e:
    print(e)
    print(22)
