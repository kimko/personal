import json

import pytest

from tests.factory import name, job, text, phone_number, email

def test_create_resumes_201(test_app_with_db):
    payload = json.dumps(
        {
            "title": job,
            "shortDescription": text,
            "name": name,
            "email": email,
            "phone": phone_number,
        }
    )
    response = test_app_with_db.post("/resumes/", data=payload)

    assert response.status_code == 201
    assert response.json()['title'] == job
    assert response.json()["name"] == name

def test_create_resumes_422_invalid_json(test_app):
    payload = json.dumps(
        {
            # "title": job,
            "shortDescription": text,
            "name": name,
            "email": email,
            "phone": phone_number,
        }
    )
    response = test_app.post("/resumes/", data=payload)
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }