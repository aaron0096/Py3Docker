from flask import Flask
import logging

logging.basicConfig(filename="record_newapp.log", level=logging.DEBUG, format="{asctime}, {levelname}, {name}, {message}".format())
app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.debug("debug log info")
    app.logger.info("Info log information")
    app.logger.warning("Warning log info")
    return 'Hello, Docker!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
