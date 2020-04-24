from flask import Flask, render_template, request
from translate import translate_sequence

app = Flask(__name__)


@app.route('/')
def translate_dna_to_protein():
    dna_sequence = request.args.get("dna_sequence", "")
    protein_sequence = translate_sequence(dna_sequence)
    return render_template("translate_dna_to_protein.html", dna_sequence=dna_sequence,
                           protein_sequence=protein_sequence)


if __name__ == '__main__':
    app.run()
