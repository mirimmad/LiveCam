#Copyright Mir Immad - RealTimeCam
class GetCamera():
	def gen(self,camera):
		while True:
			frame = camera.get_frame()
			yield (b'--frame\r\n'
				   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')		
