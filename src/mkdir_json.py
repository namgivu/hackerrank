def make_path(my_dict: dict, *paths: str) -> dict:
    """
    Boseong Choi on stackoverflow ref. https://stackoverflow.com/a/60808993/248616
    """
    while paths:
        key, *paths = paths
        my_dict = my_dict.setdefault(key, {})
    last_key_item = my_dict  # returns its deepest path ref. https://stackoverflow.com/questions/60808884/python-to-create-dict-keys-path-similarly-to-mkdir-p#comment107600642_60808993
    return last_key_item


def mkdir_json(d:'output dict', *key_path: str) -> dict:
    """
    Similar to mkdir -p but applied for json path instead of folder path ref. Boseong Choi on stackoverflow https://stackoverflow.com/a/60808993/248616

    * sample usage *
    d = json.loads('YOUR_JSON_STRING'); make_path(d, 'path-to', 'my', 'keys')
    """
    for k in key_path:
        d = d.setdefault(k, {})
