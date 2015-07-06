#!/usr/bin/python

#-Configuration--------------------------------------------------------------#

HOST = '127.0.0.1'
PORT = 8081
FOLDERS = [
    '/var/www/play.zufallston.de/dice-engine/',
    '/var/www/play.zufallston.de/dice-static/',
    '/var/www/play.zufallston.de/dice-parser/']

#----------------------------------------------------------------------------#

from subprocess import Popen, PIPE
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        output = []
        for folder in FOLDERS:
            process = Popen(['git', 'pull'], cwd=folder,
                stdout=PIPE, stderr=PIPE)
            out, err = process.communicate()
            output.append(
                'folder: %s\nstderr: %s\nstdout: %s\n' % (
                    folder, err, out))
        response = "<!DOCTYPE html><html><head><title>git</title></head>\
                    <body><pre>%s</pre></body></html>" % '\n'.join(output)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(response))
        self.end_headers()
        self.wfile.write(response)

server = HTTPServer((HOST, PORT), HTTPRequestHandler)
server.serve_forever()
