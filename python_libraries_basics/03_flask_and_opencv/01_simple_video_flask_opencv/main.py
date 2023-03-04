from flask import Flask, render_template, Response
from video import Video_Object

app = Flask(__name__)


new_object = Video_Object()

@app.route('/')
def home():
    return render_template('index.html')

def gen(video): # python file -> video.py
    while True:
        frame = video.get_frame() # method geth_frame() from class Video_Objecjt
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(new_object), # new object starts with constructor __init__
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(port=5000)