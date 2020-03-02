
def depth_print(data):
    # this solution is for every kinds of objects which extends python's built in object
    # e.g., list itself can be passsed and all of it's attributes will be printed

    def recursively_print_depth(inner_data, depth_count=1, is_class_obj=False):
        try:
            # in case a class object is passed rather than a dictionary
            inner_data = inner_data.__dict__
            is_class_obj = True
        except (AttributeError, Exception):
            pass

        # traverse dictionary
        for key, val in inner_data.items():
            try:
                _ = vars(val)
                is_class_obj = True
            except TypeError:
                pass

            print(f"{key}{':' if is_class_obj else ''} {depth_count}")  # print key & it's depth level

            try:
                # try to parse it as a class object
                recursively_print_depth(val.__dict__, depth_count=depth_count + 1, is_class_obj=True)
            except (AttributeError, Exception):
                # if exception occurs go as usual
                if isinstance(val, dict):
                    recursively_print_depth(val, depth_count=depth_count + 1)

    if isinstance(data, str) or isinstance(data, list) or isinstance(data, tuple):
        raise TypeError(f"\ndata must be of object/class object/dictionary."
                        f"\nSupplied data type --> {type(data).__name__}")

    return recursively_print_depth(data)

