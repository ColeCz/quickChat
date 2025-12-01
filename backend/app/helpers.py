def get_query(filename: str) -> str:
    path = "./queries/" + filename
    with open(path, "r") as file:
        sql = file.read()

    return sql
