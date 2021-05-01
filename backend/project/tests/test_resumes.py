from json import dumps as jdumps

from tests.factory import generate_payload

HEADERS = {"x-token": "good token"}


def test_create_resumes_201(test_app_with_db):
    payload = generate_payload()
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["title"] == payload["title"]
    assert response.json()["name"] == payload["name"]


def test_create_resumes_422_invalid_json(test_app):
    payload = generate_payload()
    bad_payload = {key: payload[key] for key in payload if key != "title"}
    response = test_app.post("/resumes/", data=jdumps(bad_payload))
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
    response = test_app.post(
        "/resumes/", data=jdumps(generate_payload()), headers={"x-token": "wrong"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "X-Token header invalid"}


def test_read_resume_200(test_app_with_db):
    payload = generate_payload()
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)
    resume_id = response.json()["id"]

    response = test_app_with_db.get(f"/resumes/{resume_id}/", headers=HEADERS)
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == resume_id
    assert response_dict["title"] == payload["title"]
    assert response_dict["name"] == payload["name"]
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
    response = test_app_with_db.post(
        "/resumes/", data=jdumps(generate_payload()), headers=HEADERS
    )
    resume_id = response.json()["id"]

    response = test_app_with_db.get("/resumes/", headers=HEADERS)
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == resume_id, response_list))) == 1


def test_remove_resume_200(test_app_with_db):
    payload = generate_payload()
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)
    resume_id = response.json()["id"]

    response = test_app_with_db.delete(f"/resumes/{resume_id}/", headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == payload | {"id": resume_id}


def test_remove_resumes_200_flag(test_app_with_db):
    payload = generate_payload()
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)

    response = test_app_with_db.delete("/resumes/?delete_all=false", headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {
        "message": "Nothing deleted. Set query parameter 'delete_all'",
        "deleted": 0,
    }


def test_remove_resumes_200_delete_all(test_app_with_db):
    payload = generate_payload()
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)

    response = test_app_with_db.delete("/resumes/?delete_all=true", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["deleted"] > 0


def test_remove_resume_404_incorrect_id(test_app_with_db):
    response = test_app_with_db.delete("/resumes/999/", headers=HEADERS)
    assert response.status_code == 404
    assert response.json()["detail"] == "Resume not found"
