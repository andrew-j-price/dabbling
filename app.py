from flask import Flask, json, jsonify, request, Response
import os
import socket


def my_app():
    app = Flask(__name__)

    @app.route('/')
    def api_root():
        return socket.gethostname() + '\n'

    @app.route("/ip", strict_slashes=False, methods=["GET"])
    def api_ip():
        return jsonify({'ip': request.remote_addr}), 200

    @app.route('/ping', strict_slashes=False, methods=["GET"])
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
