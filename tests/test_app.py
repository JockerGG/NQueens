import json 

def test_response_for_4_queens(app, client):
    res = client.get("/queens/4")
    assert 200 == res.status_code
    data = json.loads(res.get_data(as_text = True))
    assert 2 == data["numberOfSolutions"]

def test_response_for_2_queenst(app, client):
    res = client.get("/queens/2")
    assert 200 == res.status_code
    data = json.loads(res.get_data(as_text = True))
    assert 0 == data["numberOfSolutions"]