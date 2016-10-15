#!/usr/bin/python
from flask import Flask, json, Response
import optparse
import socket
import sys


app = Flask(__name__)


@app.route('/')
def api_root():
    return socket.gethostname() + '\n'


@app.route('/v1', strict_slashes=False, methods=['GET'])
def api_v1():
    payload = [
        {
            'API': 'Version 1'
        }
    ]
    data = json.dumps(payload)
    resp = Response(data, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    parser = optparse.OptionParser(usage='python app.py -p ')
    parser.add_option('-p', '--port', action='store',
                      dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port is None:
        print 'Missing required argument: -p/--port'
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
