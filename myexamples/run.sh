#!/bin/bash

set -euo pipefail

network='FeedForwardNetwork'
config='./configs/default_genome.ini'
task='task.xor'
job_no=1
generation=10
savedir='./results'
logdir='./logs'

help_message=$(cat << EOF
Usage: $0 [options]

Options:
    --network: 実験に用いるネットワークの種類を指定 (default=${network})
    --config: モデル用の設定ファイルを指定 (default=${config})
    --task: モデルに課すタスクを指定 (default=${task})
    --job_no: 並列実行数を指定 (default=${task})
    --generation: 実験を何世代行うかを指定 (default=${task})
    --savedir: 実験結果を保存するディレクトリ (default=${savedir})
EOF
)

. ../utils/parse_options.sh

savesubdir=$(echo "${task}_${network}"  | tr '.' '_')

../utils/run.pl JOB_NO=1:${job_no} ${logdir}/log.JOB_NO.txt \
    python ./example.py \
    --network $network \
    --config $config \
    --task $task \
    --generation $generation\
    --savedir $savedir/$savesubdir \
    --run_id JOB_NO