
def depth_print(data):
    def recursively_print_depth(inner_data, depth_count=1):
        for key, val in inner_data.items():
            print(key, depth_count)  # print key & it's depth level

            if isinstance(val, dict):
                recursively_print_depth(val, depth_count=depth_count + 1)

    if not isinstance(data, dict):
        raise TypeError

    return recursively_print_depth(data)


"""
Problem:
-----------------------

Write the following function’s body. A nested dictionary is passed as parameter.
You need to print all keys with their depth. 

_______________________
Sample Input: 
a = { 
“key1”: 1,
“key2”: { 
        “key3”: 1, 
        “key4”: {
                “key5”: 4 
        }
    }
} 

_______________________
Sample Output: 

key1 1 
key2 1
key3 2
key4 2
key5 3 

"""
