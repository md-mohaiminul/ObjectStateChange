import json
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from tqdm import tqdm
from datetime import timedelta
import random
import pandas as pd

splits = ['train', 'val']
df = []
for split in splits:
    json_file = f'/playpen-storage/mmiemon/ego4d/Ego4d/annotations/v1/annotations/fho_oscc-pnr_{split}.json'
    with open(json_file, 'r') as f:
        data = json.load(f)
    print(data['split'])
    data = data['clips']
    print(len(data))

    for cnt, item in enumerate(data):
        video_uid = item['video_uid']
        clip_uid = item['unique_id']
        label = 1 if item['state_change'] else 0
        path = f'/playpen-storage/mmiemon/ego4d/data/v1/fho_clips/{clip_uid}.mp4'
        row = [path, label]
        df.append(row)
        print(clip_uid, -1)

print(len(df))

df = pd.DataFrame(df)

df.to_csv(f'data/train.csv', index=False, header=False, sep=' ')

