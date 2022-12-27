"""counter=1
def get_call(counter):
    if counter >=3:
        exit()
    else:
        print("call iniated")
        counter=counter+1
        get_call(counter)

get_call(0)
"""


####
def validate_status(response_json, status):
    for key in response_json:
        if key == status:
            print("{}: {}".format(status, response_json[key]))
            if response_json[key]=='completed':
                return 'Success'
            else:
                validate_status(response_json[key], status)


json_object = {"key1": "val1", "key2": [{"key3":"val3", "key4": "val4"}, 123, "abc"]}
target_key = "key3"
validate_status(response_json=json_object,status='key3')