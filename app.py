from flask import Flask, jsonify, render_template
import pandas as pd
from transformers import pipeline


def load_generator():
    return pipeline("text2text-generation", model="valhalla/t5-small-qg-prepend")


def load_dataset(path="clean_general_aptitude_dataset.csv"):
    return pd.read_csv(path, sep=';')


def create_app(generator=None, dataframe=None):
    app = Flask(__name__, template_folder="templates")

    app.config["GENERATOR"] = generator
    app.config["DATAFRAME"] = dataframe

    def get_generator():
        if app.config["GENERATOR"] is None:
            app.config["GENERATOR"] = load_generator()
        return app.config["GENERATOR"]

    def get_dataframe():
        if app.config["DATAFRAME"] is None:
            app.config["DATAFRAME"] = load_dataset()
        return app.config["DATAFRAME"]

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/generate', methods=['GET'])
    def generate_question():
        df = get_dataframe()
        question_generator = get_generator()

        context = df['Question'].sample(1).iloc[0]
        generated = question_generator("generate question: " + context)
        question = generated[0]['generated_text']

        row = df[df['Question'] == context].iloc[0]
        options = [row['Option A'], row['Option B'], row['Option C'], row['Option D']]
        answer = row['Answer']

        return jsonify({
            "question": question,
            "options": options,
            "answer": answer
        })

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
