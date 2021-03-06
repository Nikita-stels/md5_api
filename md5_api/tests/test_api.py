def check_response(response, data=None, status_code=200):
    assert response.status_code == status_code
    if data:
        assert response.json == data


# POST
def test_create_task(test_client, init_database, mocker):
    mocker.patch('md5_api.tasks.calculate_hash_by_url_task')
    mocker.patch('md5_api.schema.get_task_id', lambda: 'test_create_task')

    response = test_client.post(
        '/submit', data={'email': 'nikolai.semenov.work@gmail.com', 'url': 'http://25.io/toau/audio/sample.txt'},
    )
    check_response(response, {'id': 'test_create_task'}, 201)


def test_create_task_wo_email(test_client, init_database, mocker):
    mocker.patch('md5_api.tasks.calculate_hash_by_url_task')
    mocker.patch('md5_api.schema.get_task_id', lambda: 'test_create_task_wo_email')

    response = test_client.post(
        '/submit', data={'url': 'http://25.io/toau/audio/sample.txt'},
    )
    check_response(response, {'id': 'test_create_task_wo_email'}, 201)


def test_create_task_invalid_email(test_client, init_database):
    response = test_client.post(
        '/submit', data={'email': 'user@example', 'url': 'http://25.io/toau/audio/sample.txt'},
    )
    check_response(response, {'errors': {'email': ['Not a valid email address.']}}, 400)


def test_create_task_wo_url(test_client, init_database):
    response = test_client.post(
        '/submit', data={'email': 'nikolai.semenov.work@gmail.com'},
    )
    check_response(response, {'errors': {'url': ['Missing data for required field.']}}, 400)


def test_create_task_invalid_url(test_client, init_database):
    response = test_client.post(
        '/submit', data={'email': 'nikolai.semenov.work@gmail.com', 'url': 'site.com/file.txt'},
    )
    check_response(response, {'errors': {'url': ['Not a valid URL.']}}, 400)


def test_create_wo_data(test_client, init_database):
    response = test_client.post('/submit')
    check_response(response, {'errors': {'url': ['Missing data for required field.']}}, 400)


# GET
def test_get_created_task(test_client, init_database):
    response = test_client.get('/check?id=created123')
    check_response(response, {'status': 'created'})


def test_get_running_task(test_client, init_database):
    response = test_client.get('/check?id=running123')
    check_response(response, {'status': 'running'})


def test_get_fail_task(test_client, init_database):
    response = test_client.get('/check?id=fail123')
    check_response(response, {'status': 'fail'})


def test_get_done_task(test_client, init_database):
    response = test_client.get('/check?id=done123')
    check_response(response, {'status': 'done', 'url': 'http://25.io/toau/audio/sample.txt', 'md5': 'hash'})


def test_get_not_found_task(test_client, init_database):
    response = test_client.get('/check?id=notfound123')
    check_response(response, {'status': 'not found'}, 404)


def test_get_wo_id_task(test_client, init_database):
    response = test_client.get('/check')
    check_response(response, {'status': 'not found'}, 404)
