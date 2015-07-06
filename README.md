# Server at *.zufallston.de

This is the server we got from Catalyst for the hackaton. You can deploy any
changes in the github-repos to the server by going to
http://pull.zufallston.de (wich triggers the `pull-them-all.py`-script in this
repository).

The default user to login per `ssh` is `hacker46`, you can authenticate per
password or add your public ssh-key to `authorized_keys` (if you don't have
the password).

## sites-available

This folder contains configs for the `nginx`-server, adding files here has no
effect, since they need to be linked to `sites-enabled` on the server.

### play.zufallston.de

The "game" is available at http://play.zufallston.de. Change the file in this
repo to change the routing between static files ("the frontend") and the
dice-engine.

### pull.zufallston.de

Pull changes from github and restart the server (if `nginx -t` succeeds, I'm
not mad). You should not need to change the config for this. You may however
want to improve the python script handling the requests.
