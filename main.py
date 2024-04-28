def convertCurrentType(value):
    if value.lower() == "false":
        return False
    
    if value.lower() == "true":
        return True
    
    # try convert to int
    try:
        return int(value)
    except ValueError:
        pass
    
    # try convert to float
    try:
        return float(value)
    except ValueError:
        pass
    return value

if __name__ == "__main__":
    print("hello world")