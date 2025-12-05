def callLimit(limit: int):
    """Call limit decorator"""
    if not isinstance(limit, int) or limit <= 0:
        print("ERROR: limit must be a positive integer")
        return None

    def callLimiter(function):
        """Call limiter function"""
        count = 0
        if not function or not callable(function):
            print("ERROR: function is not a function")
            return None

        def limit_function():
            """Limit function"""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function()
        return limit_function
    return callLimiter
