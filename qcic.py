import picamera
import datetime
import os

delcount = 2

def check_fs():
    global delcount

    st = os.statvfs('/')
    pct = 100 - st.f_bavail * 100.0 / st.f_blocks
    print pct, "percent full"
    
    if pct > 90:
        # less than 10% left, delete a few minutes
        files = os.listdir('.')
        files.sort()

        for i in range(0, delcount):
            print "deleting", files[i]
            os.remove(files[i])
        delcount += 1   # keep increasing until we get under 90%
    else:
        delcount = 2

with picamera.PiCamera() as camera:
    try:
        check_fs()
        tstamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        print "recording", tstamp
        camera.start_recording(tstamp + '.h264')
        camera.wait_recording(60)
        while True:
            check_fs()
            tstamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
            print "recording", tstamp
            camera.split_recording(tstamp + '.h264')
            camera.wait_recording(60)

    except KeyboardInterrupt:
        print "quitting"
    camera.stop_recording()

