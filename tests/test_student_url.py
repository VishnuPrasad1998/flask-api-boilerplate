from __future__ import print_function  # Use print() instead of print
from app.models.student import StudentModel
from app import db

def test_page_urls(client):
    # Visit home page
    response = client.get('/student')
    assert response.status_code==200

def test_ctype(client):
    response = client.get('/student')
    assert response.content_type=="application/json"

def test_stud(client):
    u = StudentModel(name="vp", course="cse")
    db.session.add(u)
    db.session.commit()
    v = StudentModel(name="nkp", course="ece")
    db.session.add(v)
    db.session.commit()
    one_stud = StudentModel.query.filter(StudentModel.course == "cse").one()
    assert one_stud.name == "vp"