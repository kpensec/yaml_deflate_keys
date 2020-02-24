from __future__ import print_function

"""
  deflating key from yaml file with '.' in keys

  best effort dict are merge, already parent parsed parent key are replaced
"""

def usage():
    print(f"{__file__} <yaml file>")

def _deflate_dict(data: dict):
    result = {}
    for k,v in data.items():
        splited_key = k.split('.')
        if len(splited_key) == 1:
            result[k] = deflate(v)
        else:
            result[splited_key[0]] = result.get(splited_key[0], {})
            subresult = result[splited_key[0]]
            # fetch subkey and alloca missing ones
            for subk in splited_key[1:-1]:
                subresult[subk] = subresult.get(subk, {})
                subresult = subresult[subk]
            subresult[splited_key[-1]] = deflate(v)

    return result


def deflate(data):
    return {
        dict: _deflate_dict,
        list: lambda x: list(map(deflate,x))
    }.get(type(data), lambda x:x)(data)

def main(argv):
    data = {
        "a.b": [{"d.e": 2}, {"d.f": 4}],
        "a.g": "testing",
        "a.h.f.a.b": 42,
        "a.h.f.b.c": 42,
        "a.h.g": 42,
        "b": 14,
        "c": "testing string",
        "g": {"a.f.g": 42},
        "g": {"a":{"f":{"z":5}}},
        "g": {"borzaz": 55},
    }

    return deflate(data)
        

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
