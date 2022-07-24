import json
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from tqdm import tqdm
from datetime import timedelta
import random

json_file = '/playpen-storage/mmiemon/ego4d/Ego4d/annotations/v1/annotations/fho_oscc-pnr_test_unannotated.json'
with open(json_file, 'r') as f:
    data = json.load(f)
print(data['split'])
data = data['clips']
print(len(data))

random.shuffle(data)

durations = []
cnt = 0
for item in tqdm(data):
    cnt += 1
    video_uid = item['video_uid']
    clip_uid = item['unique_id']
    video_file = f'/playpen-storage/mmiemon/ego4d/data/v1/full_scale_fps_3/{video_uid}.mp4'
    save_path = f'/playpen-storage/mmiemon/ego4d/data/v1/fho_clips/{clip_uid}.mp4'
    if os.path.exists(save_path):
        continue
    start = item['parent_start_sec']
    duration = item['parent_end_sec'] - item['parent_start_sec']
    durations.append(duration)
    print(cnt, video_uid, clip_uid, duration)

    start = timedelta(seconds=start)
    duration = timedelta(seconds=duration)
    cmd = f'ffmpeg -ss {start} -t {duration} -i {video_file} {save_path}'
    print(cmd)
    os.system(cmd)

print(min(durations), max(durations), sum(durations)/len(durations))