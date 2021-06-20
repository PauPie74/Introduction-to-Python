def unique_dictionary(dictionary):
    unique_dictionary = dict()
    for key,value in dictionary.items():
          if value not in unique_dictionary.values():
            unique_dictionary[key] = value
    return unique_dictionary