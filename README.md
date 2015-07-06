# Server at *.zufallston.de

## sites-available

### play.zufallston.de

The "game" is available at http://play.zufallston.de". Change the file in this
repo to change the routing between static files ("the frontend") and the
dice-engine.

### pull.zufallston.de

Pull changes from github and restart the server (if `nginx -t` succeeds, I'm
not mad). You should not need to change the config for this. You may however
want to improve the python script handling the requests.
