class Parser:
    def convertCurrentType(self, value):
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