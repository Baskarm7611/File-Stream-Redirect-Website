from flask import Flask, redirect , request
import os
app = Flask(__name__)

WEBSITE_DOMAIN = os.environ.get('WEBSITE_DOMAIN')

# Defining the home page of our site
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>') 
def home(path):
    url = request.url.replace(request.host, WEBSITE_DOMAIN)
    return redirect(url) # some basic inline html


if __name__ == "__main__":
    app.run(port=8000)