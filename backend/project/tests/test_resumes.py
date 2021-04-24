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
    assert "id" in response.json()
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

def test_read_resume_200(test_app_with_db):
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
    resume_id = response.json()["id"]

    response = test_app_with_db.get(f"/resumes/{resume_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == resume_id
    assert response_dict["title"] == job
    assert response_dict["name"] == name
    assert response_dict["created_at"]

def test_read_resume_404_not_found(test_app_with_db):
    response = test_app_with_db.get(f"/resumes/999/")

    assert response.status_code == 404
    assert response.json()["detail"] == "Resume not found"

def test_read_all_resumes_200(test_app_with_db):
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
    resume_id = response.json()["id"]

    response = test_app_with_db.get("/resumes/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == resume_id, response_list))) == 1
