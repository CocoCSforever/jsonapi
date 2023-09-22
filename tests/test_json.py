import json

SAMPLE_COMPLEX = complex(5, 8)
SAMPLE_RANGE  = range(1, 8, 4)
SAMPLE_DATA = {
    "Yijia": complex(1, 2),
    "Ma": range(1, 10, 3),
    "6666": True,
}
SAMPLE_LIST = [1, 5, 8, 10]
SAMPLE_DICT = {"author": "yijia", "no idea": "yes"}
SAMPLE_STR = "asfhiabf 129765bbbbb"
SAMPLE_INT =  1989664
SAMPLE_FLOAT = 1.9384
SAMPLE_BOOL = True
SAMPLE_OBJ = None

def test_customized_data():
    try:
        json.dumps(SAMPLE_COMPLEX)
    except TypeError:
        # If a TypeError is raised, this block will execute
        assert True
    else:
        # If no error is raised, this block will execute
        assert False, "Expected a ValueError but no error was raised."

    try:
        json.dumps(SAMPLE_RANGE)
    except TypeError:
        # If a TypeError is raised, this block will execute
        assert True
    else:
        # If no error is raised, this block will execute
        assert False, "Expected a ValueError but no error was raised."
    
    try:
        json.dumps(SAMPLE_DATA)
    except TypeError:
        # If a TypeError is raised, this block will execute
        assert True
    else:
        # If no error is raised, this block will execute
        assert False, "Expected a ValueError but no error was raised."
    

def test_data():
    encoded_LIST = "[1, 5, 8, 10]"
    encoded_DICT = "{\"author\": \"yijia\", \"no idea\": \"yes\"}"
    encoded_STR = '"asfhiabf 129765bbbbb"'
    encoded_INT = "1989664"
    encoded_FLOAT = "1.9384"
    encoded_BOOL = "true"
    encoded_OBJ = "null"

    # test json.dumps()
    assert(
        json.dumps(SAMPLE_LIST) == encoded_LIST
        and json.dumps(SAMPLE_DICT) == encoded_DICT
        and json.dumps(SAMPLE_STR) == encoded_STR
        and json.dumps(SAMPLE_INT) == encoded_INT
        and json.dumps(SAMPLE_FLOAT) == encoded_FLOAT
        and json.dumps(SAMPLE_BOOL) == encoded_BOOL
        and json.dumps(SAMPLE_OBJ) == encoded_OBJ
    )
    
    # test json.loads()
    assert(
        json.loads(encoded_LIST) == SAMPLE_LIST
        and json.loads(encoded_DICT) == SAMPLE_DICT
        and json.loads(encoded_STR) == SAMPLE_STR
        and json.loads(encoded_INT) == SAMPLE_INT
        and json.loads(encoded_FLOAT) == SAMPLE_FLOAT
        and json.loads(encoded_BOOL) == SAMPLE_BOOL
        and json.loads(encoded_OBJ) == SAMPLE_OBJ
    )

