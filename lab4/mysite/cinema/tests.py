import requests


def test_home_page():
    url = 'http://127.0.0.1:8000/'
    response = requests.get(url)
    assert response.status_code == 200


def test_about_page():
    url = 'http://127.0.0.1:8000/about/'
    response = requests.get(url)
    assert response.status_code == 200


def test_film_page_1():
    url = 'http://127.0.0.1:8000/film/1/'
    response = requests.get(url)
    assert response.status_code == 200


def test_film_page2():
    url = 'http://127.0.0.1:8000/film/2/'
    response = requests.get(url)
    assert response.status_code == 200


def test_film_page3():
    url = 'http://127.0.0.1:8000/film/222/'
    response = requests.get(url)
    assert response.status_code == 404


def test_genre_page1():
    url = 'http://127.0.0.1:8000/genre/3/'
    response = requests.get(url)
    assert response.status_code == 200


def test_genre_page2():
    url = 'http://127.0.0.1:8000/genre/11/'
    response = requests.get(url)
    assert response.status_code == 200


def test_genre_page3():
    url = 'http://127.0.0.1:8000/genre/257/'
    response = requests.get(url)
    assert response.status_code == 404


def test_hall_page():
    url = 'http://127.0.0.1:8000/halls/'
    response = requests.get(url)
    assert response.status_code == 200


def test_hall_page():
    url = 'http://127.0.0.1:8000/emploeeys/'
    response = requests.get(url)
    assert response.status_code == 200


def test_not_found_page():
    url = 'http://127.0.0.1:8000/emploeeys/hahaha'
    response = requests.get(url)
    assert response.status_code == 404


def test_buy_ticket_page():
    url = 'http://127.0.0.1:8000/buyticket/'
    response = requests.get(url)
    assert response.status_code == 404


def test_ticket_page():
    url = 'http://127.0.0.1:8000/tickets/'
    response = requests.get(url)
    assert response.status_code == 404


def test_return_ticket_page():
    url = 'http://127.0.0.1:8000/tickets/deletetickets.html'
    response = requests.get(url)
    assert response.status_code == 404


def test_update_ticket_page():
    url = 'http://127.0.0.1:8000/tickets/changetickets.html'
    response = requests.get(url)
    assert response.status_code == 404