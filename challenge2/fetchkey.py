import sys
from metadata import get_metadata

def dict_extract(key, var):
        if hasattr(var, 'items'):
            for k, v in var.items():
                if k == key:
                    yield v
                if isinstance(v, dict):
                    for result in dict_extract(key, v):
                        yield result
                elif isinstance(v, list):
                    for d in v:
                        for result in dict_extract(key, d):
    
                            yield result

            
def find_key(key):
    metadata = get_metadata()
    return list(dict_extract(key, metadata))
for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])

if __name__ == '__main__':
    print(find_key(sys.argv[i]))
