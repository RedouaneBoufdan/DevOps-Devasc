from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")

        if user == "cisco" and pwd == "Cisco123!":
            return redirect(url_for("success"))
        else:
            error = "Invalid credentials"

    return render_template("login.html", error=error)

@app.route("/success")
def success():
    return "Login successful"

if __name__ == "__main__":
    app.run(debug=True)
