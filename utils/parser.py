def parse_user_input(value):
    if value is None or (isinstance(value, str) and value.strip() == ""):
        raise ValueError("Input cannot be empty or None")
    if isinstance(value, str):
        return value.strip()
    return value    

def parse_to_machine_format(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    parsed_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            parsed_data[key] = value.strip().lower()
        elif isinstance(value, int):
            parsed_data[key] = value
        else:
            parsed_data[key] = value
    return parsed_data

def parse_db_record(record):
    if not isinstance(record, dict):
        raise ValueError("Input must be a dictionary")
    if not record:
        raise ValueError("Input dictionary cannot be empty")
    parsed_record = {}
    for key, value in record.items():
        if value is None:
            parsed_record[key] = ""      # handle None gracefully
        elif isinstance(value, str):
            parsed_record[key] = value.strip().capitalize()
        elif isinstance(value, int):
            parsed_record[key] = str(value)
        else:
            parsed_record[key] = value
    return parsed_record