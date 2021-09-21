#!/usr/bin/env python

import uuid
import os
import requests

URL = os.environ.get('GUESTBOOK_URL')


def test_e2e():
    assert URL
    print("Running test against {}".format(URL))
    r = requests.get(URL)
    assert b'Guestbook' in r.content
    u = uuid.uuid4()
    data = {'content': str(u)}
    r = requests.post(URL + '/sign', data)
    assert r.status_code == 200
    r = requests.get(URL)
    assert str(u).encode('utf-8') in r.content
    print("Success")


if __name__ == "__main__":
    test_e2e()
