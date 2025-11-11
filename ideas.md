1. make the slug be generated on ots own, to make it unique add user or project id in url
2. make sure that requests come to owner and he accepts or rejects the requests.
3. when deleting an object delete all related docs as well. Ex. when removing user remove its projects also
4. i want a responce handler that can be used in routes to generate a standard response. like below
    ```python
    def success(data=None, message="Success"):
    return {"success": True, "data": data, "message": message}

    def error(message="Something went wrong", code=400):
    return {"success": False, "error": {"message": message, "code": code}}
    ```