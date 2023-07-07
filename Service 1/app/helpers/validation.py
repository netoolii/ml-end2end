def text_validation(min_length: int = 10):
    def validate(value):
        if not isinstance(value, str):
            raise ValueError("Input payload is not a string")
        if len(value) < min_length:
            raise ValueError("the minimum string length is 10")
        return value

    return validate
