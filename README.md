md5_api
============
Web service for internet files md5 hash calculating  

Installing
============
You need docker:
* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)

Docker images preparation:

```sh
docker-compose build
```

Running
============
Command to run service:
```sh
docker-compose up -d
```

restarting:
```sh
docker-compose restart
```

stopping:
```sh
docker-compose stop
```


Running the tests:
```sh
docker exec -it api py.test
```

Usage
============

Usage examples:
```sh
>>> curl -X POST -d "email=user@example.com&url=http://25.io/toau/audio/sample.txt" http://localhost:8000/submit
{"id":"0e4fac17-f367-4807-8c28-8a059a2f82ac"}

>>> curl -X GET http://localhost:8000/check?id=0e4fac17-f367-4807-8c28-8a059a2f82ac
{"md5":"f4afe93ad799484b1d512cc20e93efd1","status":"done","url":"http://25.io/toau/audio/sample.txt"}
```

