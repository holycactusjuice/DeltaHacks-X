from flask import request, Blueprint, render_template, url_for, session, jsonify

# from . import openAI_client
from .summarizer import Summarizer

views = Blueprint("views", __name__)


@views.route('/get-summary', methods=['POST'])
def get_summary():

    data = request.json
    url = data.get('url')
    start_time = Summarizer.timestamp_to_seconds(str(data.get('startTime')))
    end_time = Summarizer.timestamp_to_seconds(str(data.get('endTime')))
    word_count = int(data.get('wordCount'))

    summary = Summarizer.getFinalsummary(url, word_count, start_time, end_time)

    title = Summarizer.get_video_title(url)

    if not url:
        return jsonify({"error": "No URL provided"})

    return jsonify({"title": title, "url": url, "text": summary})
