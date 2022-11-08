import json


def iterate(inputObject, key):
    splitKeys = key.split('/')
    try:
        value = inputObject[splitKeys[0]]
        for key in splitKeys[1:]:
            value = value[key]
        return value
    except Exception as err:
        print("Key value not present")
        return None


def validate_format(inputObject):
    try:
        json.loads(inputObject)
        return True
    except Exception as err:
        return False


if __name__ == '__main__':
    nestJSON = input('Enter a nested JSON object :')
    if validate_format(nestJSON):
        inputKEY = input('Enter the key in format x/y :')
        print("the value of key is", iterate(json.loads(nestJSON), inputKEY))
    else:
        print("wrong input json is provided")
