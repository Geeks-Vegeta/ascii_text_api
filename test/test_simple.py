import sys
import os
value = os.path.dirname(os.path.abspath("app.py"))
sys.path.append(value)

from app import app


def test_intial_route():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_fail_ascii_route():
    try:
        response = app.test_client().get("/ascii_pre")
        assert response.status_code == 200
    except Exception:
        assert Exception

def test_ascii_route():
    response = app.test_client().get("/ascii_pre?query=shreyas&fonts=bulbhead")
    assert response.status_code == 201
   

def test_ascii2_route():
    response = app.test_client().get("/ascii?query=shreyas&fonts=bulbhead")
    assert response.status_code == 200
   
