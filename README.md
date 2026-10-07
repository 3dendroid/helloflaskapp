# helloflaskapp
 
A minimal Flask web application that greets you. Built to practice containerizing a Python app with Docker and publishing the image to Docker Hub.
 
## Endpoints
 
| Route | Response |
|-------|----------|
| `/` | Static greeting: `Hello!` |
| `/hello there` (URL: `/hello%20there`) | Random greeting from a fixed list (`Hi there!`, `Greetings!`, `Howdy!`, ...) |
 
The app listens on `0.0.0.0:5000`.
 
## Run locally
 
Requirements: Python 3 and Flask.
 
```bash
pip install flask
python3 app.py
```
 
Check it:
 
```bash
curl http://localhost:5000/
curl http://localhost:5000/hello%20there
```
 
## Run with Docker
 
Build the image:
 
```bash
docker build -t <your-dockerhub-username>/helloflaskapp:latest .
```
 
Run a container (host port 5000 -> container port 5000):
 
```bash
docker run -d -p 5000:5000 <your-dockerhub-username>/helloflaskapp:latest
```
 
Verify:
 
```bash
docker ps
curl http://localhost:5000/
```
 
## Publish to Docker Hub
 
```bash
docker login
docker push <your-dockerhub-username>/helloflaskapp:latest
```
 
## Pull and run from Docker Hub
 
```bash
docker pull <your-dockerhub-username>/helloflaskapp:latest
docker run -d -p 5000:5000 <your-dockerhub-username>/helloflaskapp:latest
```
 
## Project structure
 
```
helloflaskapp/
├── app.py        # Flask application
├── Dockerfile    # Image definition
└── README.md
```
 
## Notes
 
- The container must bind to `0.0.0.0` (not `127.0.0.1`), otherwise the published port is unreachable from the host. `app.py` already does this.
- To use a different host port, change the left side of the mapping, e.g. `-p 8080:5000`.