import os
import socket
import time
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
START_TIME = time.time()

# Nome do Web App definido via variável de ambiente
WEBAPP_NAME = os.getenv("WEBAPP_NAME", "WebApp")

def instance_info():
    return {
        "hostname": socket.gethostname(),
        "website_instance_id": os.getenv("WEBSITE_INSTANCE_ID"),
        "python_version": os.sys.version.split()[0],
        "client_ip": request.headers.get("X-Forwarded-For", request.remote_addr),
        "webapp_name": WEBAPP_NAME
    }

@app.route("/")
def index():
    return render_template(
        "index.html",
        info=instance_info(),
        uptime=round(time.time() - START_TIME, 2),
        webapp_name=WEBAPP_NAME
    )

@app.route("/healthz")
def healthz():
    return "ok", 200

@app.route("/whoami")
def whoami():
    return jsonify(instance_info())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
