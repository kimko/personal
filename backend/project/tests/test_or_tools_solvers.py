from json import dumps as jdumps

from app.utils.factory import generate_ots_payload

HEADERS = {"x-token": "good token"}


def test_create_resumes_201(test_app):
    payload = generate_ots_payload()
    response = test_app.post("/ots/", data=jdumps(payload), headers=HEADERS)
    assert response.status_code == 201
