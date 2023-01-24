def reverse(dict_keys):
    re = {}
    for key in dict_keys:
        value = dict_keys[key]
        re[value] = key
    return re


def keys(dict_keys, value):
    re = []
    for key in dict_keys:
        if dict_keys[key] == value:
            re.append(key)
    return re


exec(input().strip())