import json


def iterate(inputObject, key):
    """get the key value from the json object"""
    objectKeys = key.split('/')
    try:
        value = inputObject[objectKeys[0]]
        for key in objectKeys[1:]:
            value = value[key]
        return value
    except Exception as err:
        print("Key value not present")
        return None


def validate_input_json(inputObject):
    """validate input json object"""
    try:
        json.loads(inputObject)
        return True
    except Exception as err:
        return False


if __name__ == '__main__':
    nestJSON = input('Enter a nested JSON object :')
    if validate_input_json(nestJSON):
        inputKEY = input('Enter the key in format x/y :')
        print("the value of key is", iterate(json.loads(nestJSON), inputKEY))
    else:
        print("wrong input json is provided")
