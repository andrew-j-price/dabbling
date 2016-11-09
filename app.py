#!/usr/bin/python
from flask import Flask, json, jsonify, Response
import optparse
import socket
import sys


def my_app():
    app = Flask(__name__)

    @app.route('/')
    def api_root():
        return socket.gethostname() + '\n'

    @app.route('/ping', strict_slashes=False)
    def api_ping():
        return jsonify(ping='pong')

    @app.route('/v1', strict_slashes=False, methods=['GET'])
    def api_v1():
        payload = [{'API': 'Version 1.0.0'}]
        data = json.dumps(payload)
        resp = Response(data, status=200, mimetype='application/json')
        return resp

    @app.route('/v2', strict_slashes=False, methods=['GET'])
    def api_v2():
        payload = [{'API': 'Version 2.1.0'}]
        data = json.dumps(payload)
        resp = Response(data, status=200, mimetype='application/json')
        return resp

    return app


if __name__ == '__main__':
    app = my_app()
    parser = optparse.OptionParser(usage='python app.py -p ')
    parser.add_option('-p', '--port', action='store',
                      dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port is None:
        print('Missing required argument: -p/--port')
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
