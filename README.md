# haproxy-whiteboard

Adding a simple dashboard to HAProxt for IP whitelisting.

# Quick start (development mode)
NOTE: You need to have Docker and Docker Compose already installed and ready to use.
```
git clone https://github.com/tohu-wabohu/haproxy-whiteboard.git
cd haproxy-whiteboard
./start

./exec_whiteboard
python app.py
```
App will be exposed through http://127.0.0.1:5000

HAProxy will start listening on http://127.0.0.1. You can test whitelisting feature using provided IP on this page.
