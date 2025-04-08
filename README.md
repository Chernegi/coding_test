# coding_test


### System requirements:
- preinstalled Docker
- preinstalled Python3


### TASK: please check TODO items and try to solve them

### CLI uvicorn app launch:
```
uvicorn main:app
# app available on the https://localhost/docs
```

### build Docker image
```
docker build -t echo-chatbot .
```

### run Docker container
```
docker run -p 8000:8000 echo-chatbot
```

### chat-bot test:
```
curl -X POST "http://localhost:8000/echo" -H "Content-Type: application/json" -d '{"message": "Hello, world!"}'
```