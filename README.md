
# FastAPI with React 

A Basic Setup of FastAPI with React on the Frontend and Mongo DB for Backend with Docker Setup.

## Tech Stack:

-   [FastAPI](https://fastapi.tiangolo.com/)  - FastAPI framework, high performance, easy to learn, fast to code, ready for production.
-   [Mongo DB](https://www.mongodb.com)  - Build the next big thing.
-   [React Js](https://reactjs.org)  - A JavaScript library for building user interfaces.
-   [Carbon Design System](https://carbondesignsystem.com/)  - Carbon is IBM’s open source design system for products and digital experiences.
-   [Docker](https://www.docker.com/)  - Docker is a platform designed to help developers build, share, and run modern applications. We handle the tedious setup, so you can focus on the code.


## Get Started

Cloning The Repo:
```bash
$ mkdir ~/Dev/fastapi-react
$ cd ~/Dev/fastapi-react
$ git clone https://github.com/Arvind-4/FastAPI-with-React .
$ python3.9 -m virtualenv .
$ source bin/activate
```

Create a **.env**:
```bash
$ touch ~/Dev/fastapi-react/.env
$ cp -r .sample.env .env
```

Add Your Credentials to **.env**


Run Backend Server
```bash
(fastapi-react) $ cd backend
(fastapi-react) $ pip install -r requirements.txt
(fastapi-react) $ bash run.sh
```
**For Windows use**
```bash
(fastapi-react) $ .\run.sh
```
<div align="center">
<br/>
<b>Or</b>
<br/>
</div>

```bash
(fastapi-react) $ uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Run Frontend
```bash
(fastapi-react) $ cd frontend
(fastapi-react) $ npm install
(fastapi-react) $ npm run start
```

Build The Frontend
```bash
(fastapi-react) $ npm run build
```


Using Docker-Compose:
```bash
docker-compose up --build
```
