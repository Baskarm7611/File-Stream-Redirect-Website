from flask import Flask, redirect , request
import os
app = Flask(__name__)

WEBSITE_DOMAIN = os.environ.get('WEBSITE_DOMAIN')
PORT = int(os.environ.get('PORT', 80))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>') 
def home(path):
    url = request.url.replace(request.host, WEBSITE_DOMAIN)
    return redirect(url) 


if __name__ == "__main__":
    app.run(port=PORT)