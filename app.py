from flask import Flask, render_template, redirect, flash, request, send_from_directory
import werkzeug.utils

app = Flask(__name__)
app.config["SECRET_KEY"] = "ndsnfuoewnfiuersn"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cdn-upload")
def uplp():
    return render_template("cdn-upl.html")


@app.route("/upload",methods=["POST"])
def upl():
    file = request.files["stream"]
    file.save("storage/"+werkzeug.utils.secure_filename(file.filename))
    return redirect(f"/cdn/{werkzeug.utils.secure_filename(file.filename)}")


@app.route("/cdn/<path:filename>")
def cdn(filename):
    return send_from_directory("storage",filename)

if __name__ == "__main__":
    app.run("0.0.0.0",80)
