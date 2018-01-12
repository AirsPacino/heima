def application(env, start_response):
    status = "404 NOT FOUND"
    headers = []
    start_response(status, headers)
    return "this file not found"


