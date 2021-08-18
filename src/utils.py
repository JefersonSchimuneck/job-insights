def get_unique_key_values(key_name, dict):
    unique_values = set(key[key_name] for key in dict if key[key_name])
    return unique_values
