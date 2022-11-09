
import time

import requests


METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1/'
METADATA_HEADERS = {'Metadata-Flavor': 'Google'}


def main():
    url = METADATA_URL + 'instance'
    r = requests.get(
        url,
        headers=METADATA_HEADERS)
    return r.text


if __name__ == '__main__':
    main()
    print(main())
    
# [END all]
