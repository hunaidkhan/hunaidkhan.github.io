from flask import Flask
from flask.json import jsonify
from flask_restful import Api, Resource
from youtube_transcript_api import YouTubeTranscriptApi
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, videoId):
        srt = YouTubeTranscriptApi.get_transcript(videoId,languages=['en'])
        out_file = open("data/subtitles.json", "w")
        out_file.truncate(0)
        json.dump(srt, out_file, indent = 4, sort_keys = False)
        out_file.close()
        return jsonify(srt)

    # def post(self, videoId):
    #     srt = YouTubeTranscriptApi.get_transcript(videoId,languages=['en'])
    #     return jsonify(srt)

api.add_resource(HelloWorld, "/hello/<string:videoId>")

if __name__ == "__main__":
    app.run(debug=True)