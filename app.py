from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/om')
def om():
    return render_template("om.html")

@app.route('/', methods=["GET", "POST"])
def index():
    alder = ["barn (3-12)", "ungdom (13-17)", "voksen (18+)"]
    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]

        if navn != "" and epost != "":

    
            return render_template(
                "resultat.html",
                navn=navn,
                epost=epost,
                
            )
    print(alder)
    return render_template("index.html", alder=alder)

@app.route('/resultat')
def resultat():
    return render_template("resultat.html")


if __name__ == '__main__':
    app.run(debug=True)