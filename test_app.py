from flask import url_for


class TestApp:

    def test_root(self, client):
        res = client.get(url_for('api_root'))
        assert res.status_code == 200

    def test_ping(self, client):
        res = client.get(url_for('api_ping'))
        assert res.status_code == 200
        assert res.json == {'ping': 'pong'}

    def test_v1(self, client):
        res = client.get(url_for('api_v1'))
        assert res.status_code == 200

    def test_v2(self, client):
        res = client.get(url_for('api_v2'))
        assert res.status_code == 200
