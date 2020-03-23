def make_path(d: dict, *path: str) -> dict:
    """
    Boseong Choi on stackoverflow ref. https://stackoverflow.com/a/60808993/248616
    """
    for key in path:
        d = d.setdefault(key, {})
    return d


def make_path2(my_dict: dict, *paths: str) -> dict:
    """
    Boseong Choi on stackoverflow ref. https://stackoverflow.com/a/60808993/248616
    """
    while paths:
        key, *paths = paths
        my_dict = my_dict.setdefault(key, {})
    return my_dict


