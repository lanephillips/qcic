import picamera
import datetime

with picamera.PiCamera() as camera:
    tstamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
    camera.start_recording(tstamp + '.h264')
    camera.wait_recording(5)
    for i in range(0, 11):
        tstamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
        camera.split_recording(tstamp + '.h264')
        camera.wait_recording(5)
    camera.stop_recording()

