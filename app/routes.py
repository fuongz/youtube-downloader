from flask import send_file, request, current_app as app
from flask.json import jsonify
from pytube import YouTube
import logging
from io import BytesIO


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/watch", methods=["GET"])
def downloadYoutubeVideo():
    try:
        args = request.args
        video_id = args.get("v")
        if video_id is None:
            return jsonify(error="No video id provided"), 400
        buffer = BytesIO()
        url = "https://www.youtube.com/watch?v=" + video_id
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=video.title + '.mp4', mimetype="video/mp4")
    except:
        logging.exception("Failed to download video")
        return jsonify(error="Failed to download video"), 500
