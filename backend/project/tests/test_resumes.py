from json import dumps as jdumps

from tests.factory import generate_payload

HEADERS = {"x-token": "good token"}


def test_create_resumes_201(test_app_with_db):
    # TODO this delete should not be necessary. remove all records on teardown
    response = test_app_with_db.delete("/resumes/?delete_all=true", headers=HEADERS)
    payload = generate_payload()
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["title"] == payload["title"]
    assert response.json()["name"] == payload["name"]
    assert response.json()["summary"] == payload["summary"]


def test_create_resumes_201_no_optional_values(test_app_with_db):
    # TODO this delete should not be necessary. remove all records on teardown
    response = test_app_with_db.delete("/resumes/?delete_all=true", headers=HEADERS)
    payload = generate_payload()
    payload = {key: payload[key] for key in payload if key != "summary"}
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["title"] == payload["title"]
    assert response.json()["name"] == payload["name"]


def test_create_resumes_422_public_id_not_unique(test_app_with_db):
    # TODO this delete should not be necessary. remove all records on teardown
    response = test_app_with_db.delete("/resumes/?delete_all=true", headers=HEADERS)
    payload = generate_payload()
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)
    response = test_app_with_db.post("/resumes/", data=jdumps(payload), headers=HEADERS)

    assert response.status_code == 422
    # TODO upgrade GHA container to py3.9
    assert "unique constraint" in response.json()["detail"][0]["msg"].lower()


def test_create_resumes_422_invalid_json(test_app):
    payload = generate_payload()
    bad_payload = {key: payload[key] for key in payload if key != "title"}
    bad_payload["public_id"] = "this_is_too_long"
    response = test_app.post("/resumes/", data=jdumps(bad_payload))
    assert response.status_code == 422
    assert {
        "loc": ["header", "x-token"],
        "msg": "field required",
        "type": "value_error.missing",
    } in response.json()["detail"]
    assert {
        "loc": ["body", "public_id"],
        "msg": "ensure this value has at most 6 characters",
        "type": "value_error.any_str.max_length",
        "ctx": {"limit_value": 6},
    } in response.json()["detail"]
    assert {
        "loc": ["body", "title"],
        "msg": "field required",
        "type": "value_error.missing",
    } in response.json()["detail"]


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
    assert response_dict["summary"] == payload["summary"]
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
    # TODO upgrade GHA container to py3.9
    # assert response.json() == payload | {"id": resume_id}
    assert response.json() == {**payload, **{"id": resume_id}}


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
