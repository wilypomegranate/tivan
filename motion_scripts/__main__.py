import argparse
import datetime
import requests
import json
import time

url = 'http://localhost:8000/api'

def get_cameras():
    cameras = []
    for camera in requests.get(url + '/camera').json():
        cameras.append(camera['id'])
    return cameras

cameras = get_cameras()
JSON_HEADERS = {'Content-Type': 'application/json'}

def valid_timestamp(ts):
    try:
        return datetime.datetime.strptime(ts, '%Y%m%d%H%M%S')
    except ValueError:
        msg = "'{0}' is not a valid timestamp of %Y%m%d%H%M%S"
        raise argparse.ArgumentTypeError(msg)

def start_event(args):
    #Check for camera and create it if it doesn't exist
    if args.camera not in cameras:
        r = requests.post(url + '/camera/', \
            data=json.dumps({'id': args.camera, 'stream_url': ''}), \
            headers=JSON_HEADERS)
        if not r.ok:
            print r.text
            raise Exception('Could not add camera %d' %(args.camera))

    #Create event for camera at unique timestamp
    event = {
        'start_time': args.timestamp.strftime('%Y-%m-%dT%H:%M:%S'),
        'changed_pixels': args.changed_pixels,
        'noise_level': args.noise_level,
        'motion_area_width': args.motion_area_width,
        'motion_area_height': args.motion_area_height,
        'motion_center_x': args.motion_center_x,
        'motion_center_y': args.motion_center_y,
        'camera': args.camera
    }

    r = requests.post(url + '/event/', data=json.dumps(event), headers=JSON_HEADERS)
    if not r.ok:
        print r.text
        raise Exception('Failed to post event')

def save_picture(args):
    picture = {
        'path': args.filename,
        'timestamp': args.timestamp.isoformat(),
        'event_timestamp': args.event_timestamp.isoformat(),
        'camera': args.camera
    }

    #print json.dumps(picture)
    r = requests.post(url + '/capture_picture/', data=json.dumps(picture), headers=JSON_HEADERS)
    if not r.ok:
        print r.text
        raise Exception('Failed to post capture picture')

def start_video(args):
    time.sleep(1)
    video = {
        'path': args.filename,
        'start_time': args.timestamp.isoformat(),
        'event_timestamp': args.event_timestamp.isoformat(),
        'camera': args.camera
    }

    print json.dumps(video)
    r = requests.post(url + '/capture_video/', data=json.dumps(video), headers=JSON_HEADERS)
    if not r.ok:
        print r.text
        raise Exception('Failed to post capture video')

def end_video(args):
    time.sleep(1)
    video = {
        'path': args.filename,
        'timestamp': args.timestamp.isoformat()
    }

    print json.dumps(video)

    r = requests.put(url + '/video/path/', data=json.dumps(video), headers=JSON_HEADERS)
    if not r.ok:
        print r.text
        raise Exception('Failed to update capture video')

def end_event(args):
    time.sleep(1)
    event = {
        'event_timestamp': args.event_timestamp.isoformat(),
        'camera': args.camera,
        'timestamp': args.timestamp.isoformat()
    }

    print json.dumps(event)

    r = requests.put(url + '/event_end/', data=json.dumps(event), headers=JSON_HEADERS)
    if not r.ok:
        print r.text
        raise Exception('Failed to update event stop time')

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    start_event_parser = subparsers.add_parser('start_event')
    start_event_parser.add_argument("timestamp", type=valid_timestamp)
    start_event_parser.add_argument("camera", type=int)
    start_event_parser.add_argument("changed_pixels", type=int)
    start_event_parser.add_argument("noise_level", type=int)
    start_event_parser.add_argument("motion_area_width", type=int)
    start_event_parser.add_argument("motion_area_height", type=int)
    start_event_parser.add_argument("motion_center_x", type=int)
    start_event_parser.add_argument("motion_center_y", type=int)
    start_event_parser.set_defaults(func=start_event)
    #create_parser.add_argument("filename", type=str)

    save_picture_parser = subparsers.add_parser('save_picture')
    save_picture_parser.add_argument("event_timestamp", type=valid_timestamp)
    save_picture_parser.add_argument("camera", type=int)
    save_picture_parser.add_argument("timestamp", type=valid_timestamp)
    save_picture_parser.add_argument("filename", type=str)
    save_picture_parser.set_defaults(func=save_picture)

    start_video_parser = subparsers.add_parser('start_video')
    start_video_parser.add_argument("event_timestamp", type=valid_timestamp)
    start_video_parser.add_argument("camera", type=int)
    start_video_parser.add_argument("timestamp", type=valid_timestamp)
    start_video_parser.add_argument("filename", type=str)
    start_video_parser.set_defaults(func=start_video)

    end_video_parser = subparsers.add_parser('end_video')
    end_video_parser.add_argument("timestamp", type=valid_timestamp)
    end_video_parser.add_argument("filename", type=str)
    end_video_parser.set_defaults(func=end_video)

    event_end_parser = subparsers.add_parser('event_end')
    event_end_parser.add_argument("event_timestamp", type=valid_timestamp)
    event_end_parser.add_argument("camera", type=int)
    event_end_parser.add_argument("timestamp", type=valid_timestamp)
    event_end_parser.set_defaults(func=end_event)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
