import json

from tests.factory import email, job, name, phone_number, text

HEADERS = {"x-token": "good token"}


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
    response = test_app_with_db.post("/resumes/", data=payload, headers=HEADERS)

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["title"] == job
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
                "loc": ["header", "x-token"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "title"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_create_resumes_401_invalid_token(test_app):
    payload = json.dumps(
        {
            "title": job,
            "shortDescription": text,
            "name": name,
            "email": email,
            "phone": phone_number,
        }
    )
    response = test_app.post("/resumes/", data=payload, headers={"x-token": "wrong"})
    assert response.status_code == 401
    assert response.json() == {"detail": "X-Token header invalid"}


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
    response = test_app_with_db.post("/resumes/", data=payload, headers=HEADERS)
    resume_id = response.json()["id"]

    response = test_app_with_db.get(f"/resumes/{resume_id}/", headers=HEADERS)
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == resume_id
    assert response_dict["title"] == job
    assert response_dict["name"] == name
    assert response_dict["created_at"]


def test_read_resume_422_missing_token(test_app):
    response = test_app.get("/resumes/")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["header", "x-token"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_read_resume_404_not_found(test_app_with_db):
    response = test_app_with_db.get("/resumes/999/", headers=HEADERS)

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
    response = test_app_with_db.post("/resumes/", data=payload, headers=HEADERS)
    resume_id = response.json()["id"]

    response = test_app_with_db.get("/resumes/", headers=HEADERS)
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == resume_id, response_list))) == 1


def test_remove_resume_200(test_app_with_db):
    payload = json.dumps(
        {
            "title": job,
            "shortDescription": text,
            "name": name,
            "email": email,
            "phone": phone_number,
        }
    )
    response = test_app_with_db.post("/resumes/", data=payload, headers=HEADERS)
    resume_id = response.json()["id"]

    response = test_app_with_db.delete(f"/resumes/{resume_id}/", headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {
        "id": resume_id,
        "title": job,
        "shortDescription": text,
        "name": name,
        "email": email,
        "phone": phone_number,
    }


def test_remove_resume_404_incorrect_id(test_app_with_db):
    response = test_app_with_db.delete("/resumes/999/", headers=HEADERS)
    assert response.status_code == 404
    assert response.json()["detail"] == "Resume not found"
