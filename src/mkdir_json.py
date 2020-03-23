def make_path(d: dict, *path: str) -> dict:
    """
    Boseong Choi on stackoverflow ref. https://stackoverflow.com/a/60808993/248616
    """
    for key in path:
        d = d.setdefault(key, {})


def make_path2(my_dict: dict, *paths: str) -> dict:
    """
    Boseong Choi on stackoverflow ref. https://stackoverflow.com/a/60808993/248616
    """
    while paths:
        key, *paths = paths
        my_dict = my_dict.setdefault(key, {})
    last_key_item = my_dict  # returns its deepest path ref. https://stackoverflow.com/questions/60808884/python-to-create-dict-keys-path-similarly-to-mkdir-p#comment107600642_60808993
    return last_key_item


