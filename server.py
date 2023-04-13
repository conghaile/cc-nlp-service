from flask import Flask
from flask import request
from NLP import Thread
from DB import DB
import spacy
import json
from dotenv import load_dotenv
import os
import json

load_dotenv()
MODEL = os.getenv('MODEL')
TABLE = os.getenv('TABLE')

nlp = spacy.load(MODEL)

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/threads", methods=["POST"])
# @cross_origin
def threads():
    if request.method == "POST":
        data = request.json
        thread = Thread(data)
        thread.analyze(nlp)
        db = DB()
        db.insert(thread.thread, TABLE)
        return {
            "Status": "success"
        }