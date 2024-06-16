from pprint import pprint

from flask import Flask, render_template, request, send_file, send_from_directory

import MyFunc

app = Flask(__name__, template_folder='template')

# @app.route('/')
# def index():
#     return render_template('home.html')


@app.route('/<string:nik>', methods=['GET'])
def main(nik):
    return render_template("gps.html", data={'nik': nik})


@app.route('/gps', methods=['GET', 'POST'])
def ind():
    if request.method == 'POST':
        data = dict(request.json)
        pprint(data)
        ot = MyFunc.main(data)
        pprint(ot)
        print('_'*30)
    return ot


@app.route('/static/<string:media>')
def quests(media):
    return send_from_directory('static/anime', media)
    return render_template('quests.html')


# @app.route('/library')
# def library():
#     return render_template('library.html')


# @app.route('/videos')
# def videos():
#     return render_template('videos.html')


# @app.route('/events')
# def events():
#     return render_template('events.html')


# @app.route('/events/<int:event_id>')
# def event_detail(event_id):
#     return render_template('event_detail.html', event_id=event_id)


# @app.route('/quests/<int:quest_id>')
# def quest_detail(quest_id):
#     return render_template('quest_detail.html', quest_id=quest_id)


# @app.route('/videos/<int:video_id>')
# def video_detail(video_id):
#     return render_template('video_detail.html', video_id=video_id)


if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0")
