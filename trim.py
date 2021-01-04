import ffmpeg
import csv
import os
import sys


def trim(root_dir, out_dir, annotation_file):
    with open(annotation_file) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            classname, vid, subset, start, end, label = row
            if subset == 'testing':
                continue
            classname = classname.replace(' ', '_')
            basename = 'v_{}.mp4'.format(vid)
            folder = os.path.join(root_dir, classname)
            video_path = os.path.join(folder, basename)
            if not os.path.exists(video_path):
                continue
            stream = ffmpeg.input(video_path)
            stream = ffmpeg.trim(stream, start=start, end=end)

            folder = os.path.join(out_dir, classname)
            if not os.path.isdir(folder):
                os.mkdir(folder)
            video_path = os.path.join(folder, basename)
            stream = ffmpeg.output(stream, video_path)
            ffmpeg.run(stream, overwrite_output=True)


if __name__ == "__main__":
    trim(sys.argv[1], sys.argv[2], sys.argv[3])
