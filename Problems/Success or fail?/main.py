import requests


def check_success(url):
    r = requests.get(url)
    if 200 <= r.status_code <= 399:
        return 'Success'
    else:
        return 'Fail'
