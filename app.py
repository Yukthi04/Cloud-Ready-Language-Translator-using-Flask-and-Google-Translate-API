from flask import Flask, render_template, request
from googletrans import Translator
from languages import LANGUAGE_CODES  # Make sure this file exists and has the dictionary

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""
    src_lang = "auto"
    dest_lang = "en"

    if request.method == "POST":
        text = request.form.get("text")
        src_lang = request.form.get("src_lang", "auto")
        dest_lang = request.form.get("dest_lang", "en")

        try:
            result = translator.translate(text, src=src_lang, dest=dest_lang)
            translation = result.text
        except Exception as e:
            translation = f"Error: {e}"

    return render_template("index.html", translation=translation, languages=LANGUAGE_CODES)

if __name__ == "__main__":
    app.run(debug=True)
S



