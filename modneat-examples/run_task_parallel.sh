#!/bin/bash

set -euo pipefail

network='FeedForwardNetwork'
config_file='./configs/default_genome.ini'
task='task.xor'
job_no=1
generation=10
checkpoint_interval=100
savedir='./results'
logdir='./logs'
description=''

help_message=$(cat << EOF
Usage: $0 [options]

Options:
    --network: 実験に用いるネットワークの種類を指定 (default=${network})
    --config_file: モデル用の設定ファイルを指定 (default=${config_file})
    --task: モデルに課すタスクを指定 (default=${task})
    --job_no: 並列実行数を指定 (default=${task})
    --generation: 実験を何世代行うかを指定 (default=${task})
    --checkpoint_interval : チェックポイントを何世代ごとに保存するかを指定
    --savedir: 実験結果を保存するディレクトリ (default=${savedir})
    --comment: 実験に関するコメント・説明
EOF
)

. ../utils/parse_options.sh
echo $network
echo $config_file

savesubdir=$(echo "${task}_${network}"  | tr '.' '_')

if [ ! -d $savedir/$savesubdir/ ]; then
    mkdir $savedir/$savesubdir
fi
cp $config_file $savedir/$savesubdir/
echo $description > $savedir/$savesubdir/description.txt

../utils/run.pl JOB_NO=1:${job_no} ${logdir}/log.JOB_NO.txt \
    python ./run_task.py \
    --network $network \
    --config $config_file \
    --task $task \
    --generation $generation \
    --checkpoint_interval $checkpoint_interval \
    --savedir $savedir/$savesubdir \
    --run_id JOB_NO
