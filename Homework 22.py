

import json
import pickle

def save_object(obj, filename):
    try:
        with open(filename, 'w') as json_file:
            json.dump(obj, json_file)
    except Exception as e:
        print("Failed to serialize object using JSON:", e)
        try:
            with open(filename, 'wb') as pickle_file:
                pickle.dump(obj, pickle_file)
        except Exception as e:
            print("Failed to serialize object using pickle:", e)
            print("Object serialization failed")


data = {'key': 'value'}
filename = 'data.json'
save_object(data, filename)
