#Mir Immad - LiveCam
from flask import Flask, render_template, Response
import thread
from _camera import VideoCamera
from getcamera import GetCamera


class MainServer():
	app = Flask(__name__)
	def __init__(self):

		self.app.run(host='0.0.0.0', threaded = True, debug=True, use_reloader = False)

	@app.route('/')
	def index():

		return render_template('index.html')

	@app.route('/video_feed')

	def video_feed():
		return Response(GetCamera().gen(VideoCamera()), mimetype = 'multipart/x-mixed-replace;boundary = frame')

	@app.route('/video_feed_secondry')

	def video_feed_secondry():


		return Response(GetCamera().gen(VideoCamera_s()), mimetype = 'multipart/x-mixed-replace;boundary = frame')

	@app.route('/second_cam')
	def second_cam():
		return render_template('camera_secondry.html')


if __name__ == '__main__':
	MainServer()
	print "Live video is being streamed at localhost:5000"
