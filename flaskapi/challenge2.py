#!/usr/bin/env python3
from flask import Flask

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def hosts():
    if request.method == "POST":
        hostname = request.form.get("hostname")
        ip = request.form.get("ip")
        fqdn = requests.form.get("fqdn")
        groups.append({"hostname": hostname, "ip": ip, "fqdn": fqdn})
    return render_template("hosts.j2", groups=groups)

@app.route("/form", methods=["GET", "POST"])
def form():
    return render_template("formcollector.html.j2")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
