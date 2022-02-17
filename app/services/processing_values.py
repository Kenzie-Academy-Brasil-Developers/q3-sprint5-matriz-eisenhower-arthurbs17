from genericpath import exists
from sqlalchemy import null


def processing_values(data: dict):

    keys = data.keys()

    for key in keys:
        data[key] = data[key].lower()
    
    return data