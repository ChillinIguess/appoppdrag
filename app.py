from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/om')
def om():
    return render_template("om.html")

@app.route('/', methods=["GET", "POST"])
def index():
    alder = ["barn (3-12)", "ungdom (13-17)", "voksen (18+)"]
    feil = ""

    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]

       
        if navn == "" and epost != "":
            feil = "Du skrev ikke brukernavn"
        elif navn != "" and epost == "":
            feil = "Du skrev ikke epost"
        elif navn == "" and epost =="":
            feil = "Begge feltene mangler" 
        else:

    
            return render_template(
                "resultat.html",
                navn=navn,
                epost=epost
            )
    print(alder)
    print(feil)
    return render_template("index.html", alder=alder, feil=feil)

@app.route('/resultat')
def resultat():
    produkter = [
        {"pnavn": "silksong", "pris": 230, "beskrivelse": "Hollow Knight: Silksong"},
        {"pnavn": "Deltarune", "pris": 259, "beskrivelse": "Deltarune ch 1-5"},
        

    ]
    return render_template("resultat.html", produkter=produkter)


if __name__ == '__main__':
    app.run(debug=True)