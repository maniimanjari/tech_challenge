import sys
import requests
import json

METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1/instance/'
METADATA_HEADERS = {'Metadata-Flavor': 'Google'}

def main():
    url = METADATA_URL + key
    r = requests.get(
            url,
            headers=METADATA_HEADERS)
    return r.text

if __name__ == '__main__':
    key = sys.argv[1]
    main()
    print(main())
