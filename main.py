from __future__ import printfunction

"""
  deflating key from yaml file with '.' in keys

  best effort dict are merge, already parent parsed parent key are replaced
"""

def usage():
    print(f"{__file__} <yaml file>")

def deflate(data : Union[dict, list]:
    result = data
    return result

def main(argv):
    import yaml

    if len(argv) != 2:
        usage()
    filename = argv[1]
    
    data = yaml.load(open(filename))

    deflate_key(data)
        

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
