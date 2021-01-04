#!/bin/sh
for i in `seq 2001 1000 100000`
do
    sed -n $i,`expr $i + 999`p ./HACS_v1.1.1/HACS_clips_v1.1.1.csv > ./HACS_v1.1.1/clips_`printf %07d $i`.csv
    python download_videos.py \
    --root_dir ./data \
    --annotation_file ./HACS_v1.1.1/clips_`printf %07d $i`.csv
    rsync -ahv ./data t.hosoya@k2:/beegfs/t.hosoya/HACS_v1.1.1/train
    rm -rf ./data
done