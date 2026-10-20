from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/om')
def om():
    return render_template("om.html")

@app.route('/registrer', methods=["GET", "POST"])
def registrer():
    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        alder = request.form["alder"]
        return render_template(
            "index.html",
            navn=navn,
            epost=epost,
            alder=alder
        )
    return render_template("registrer.html")




if __name__ == '__main__':
    app.run(debug=True)