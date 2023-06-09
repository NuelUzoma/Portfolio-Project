#!/usr/bin/python3
"""
A Flask Web Application with a few endpoints to test out the CI/CD Pipeline
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start():
    """First Endpoint of the application"""
    return "Hello, you are welcome"


@app.route('/build', methods=['GET'], strict_slashes=False)
def build():
    """Retrieve the information of the latest build progress"""
    return "Build successful!!"


@app.route('/test', methods=['GET'], strict_slashes=False)
def test():
    """Retrieve all test informations"""
    return "Tests has been passed!"


@app.route('/deploy', methods=['GET'], strict_slashes=False)
def deploy():
    """Retrieve informations from docker builds"""
    return "Deployment was successful"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
