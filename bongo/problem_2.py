
def depth_print(data):
    def recursively_print_depth(inner_data, depth_count=1):
        is_class_obj = False
        try:
            # in case a class object is passed rather than a dictionary
            inner_data = inner_data.__dict__
            is_class_obj = True
        except AttributeError:
            pass

        if isinstance(inner_data, dict):
            # traverse dictionary
            for key, val in inner_data.items():
                try:
                    _ = val.__dict__
                    is_class_obj = True
                except AttributeError:
                    pass

                print(f"{key}{':' if is_class_obj else ''} {depth_count}")  # print key & it's depth level

                if isinstance(val, dict) or is_class_obj:
                    recursively_print_depth(val, depth_count=depth_count + 1)

    if not data:
        raise TypeError

    return recursively_print_depth(data)


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
person_c = Person("User", "2", person_b)

d = {
    "key1": 1,
    "key2": {
        "key3": 3,
        "key4": {
            "key5": 5,
            "user": person_c
        }
    },
    "key_last": "last",
    "key_test": ["1", 3]
}

depth_print(d)

# for k in d:
#     print("---------------------------")
#     try:
#         print(d.__dict__)
#     except Exception as e:
#         print(e.__class__)
#
#     try:
#         print(vars(d))
#     except Exception as e:
#         print(e.__class__)
#
#     print("---------------------------")

# print(person_c.__dict__)
# print(vars(person_c))

"""
:param data: Dictionary or Class Object
:return: None

* This method takes in a dictionary or a class object
* prints all the attributes with their depth
* in case of class object it prints with a ':' in between, e.g.,
            user: 3
            first_name: 4
            last_name: 4
            father: 4
            first_name: 5

  otherwise normally, e.g.,
              key1 1
              key2 1
              key3 2

* if other than dictionary or class object is passed it implicitly returns None & print Nothing
"""
#   ------------------------------------

"""
Problem:
-------------------------
Write a new function with same functionality from Question 1,
but it should be able to handle a Python object in addition to a dictionary from Question 1. 

_________________________

Sample Input:
_________________________
class Person(object):
    def __init__(self, first_name, last_name, father): 
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person(“User”, “1”, none)
person_b = Person(“User”, “2”, person_a) 

a = { 
    “key1”: 1,
    ”key2”: { 
            “key3”: 1, 
            “key4”: { “key5”: 4, 
                      “user”: person_b 
                    }
            },
} 


_________________________
Sample Output: 

key1 1 
key2 1 
key3 2 
key4 2 
key5 3 
user: 3 
first_name: 4 
last_name: 4 
father: 4 
first_name: 5 
last_name: 5 
father: 5 


"""
