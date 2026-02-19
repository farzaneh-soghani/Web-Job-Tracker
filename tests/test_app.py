import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_startseite(client):
    rv = client.get('/')
    assert rv.status_code == 200


def test_stats_page(client):
    rv = client.get('/stats')
    assert rv.status_code == 200


def test_edit_page_requires_only_template(client):
    rv = client.get('/edit')
    assert rv.status_code == 200


def test_notes_page_requires_only_template(client):
    rv = client.get('/notes')
    assert rv.status_code == 200


def test_legacy_delete_redirects(client):
    rv = client.get('/delete/0')
    assert rv.status_code in (301, 302, 308)
    assert rv.headers['Location'].endswith('/')


def test_legacy_edit_redirects_when_job_has_id(client):
    with client.session_transaction() as sess:
        sess['jobs'] = [{
            'id': 'abc123',
            'firma': 'Test',
            'position': 'Dev',
            'status': 'offen',
            'datum': '01.01.2026',
            'notes': ''
        }]

    rv = client.get('/edit/0')
    assert rv.status_code in (301, 302, 308)
    assert rv.headers['Location'].endswith('/edit?id=abc123')


def test_legacy_notes_redirects_when_job_has_id(client):
    with client.session_transaction() as sess:
        sess['jobs'] = [{
            'id': 'xyz789',
            'firma': 'Test',
            'position': 'Dev',
            'status': 'offen',
            'datum': '01.01.2026',
            'notes': ''
        }]

    rv = client.get('/notes/0')
    assert rv.status_code in (301, 302, 308)
    assert rv.headers['Location'].endswith('/notes?id=xyz789')
