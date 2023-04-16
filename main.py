from flask import Flask, redirect, request
import os
app = Flask(__name__)

DL_WEBSITE_DOMAIN = os.environ.get('DL_WEBSITE_DOMAIN')
FS_WEBSITE_DOMAIN = os.environ.get('FS_WEBSITE_DOMAIN', "https://fs.0x0.st")
PORT = int(os.environ.get('PORT', 80))


@app.route('/dl/')
def home(path):
    url = request.url.replace(f"{request.host}/dl", DL_WEBSITE_DOMAIN)
    return redirect(url)


@app.route('/fs/')
def fs_home():
    url = request.url.replace(f"{request.host}/fs", FS_WEBSITE_DOMAIN)
    return redirect(url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
