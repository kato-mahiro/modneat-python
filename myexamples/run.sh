#!/bin/bash

set -euo pipefail
ln -sf ../utils/parse_options.sh ./parse_options.sh

model='FeedForwardNetwork'
config='./configs/default_genome.ini'
task='task.xor'
job_no=1
generation=10

help_message=$(cat << EOF
Usage: $0 [options]

Options:
    --model: 実験に用いるモデルを指定 (default=${model})
    --config: モデル用の設定ファイルを指定 (default=${config})
    --task: モデルに課すタスクを指定 (default=${task})
    --job_no: 並列実行数を指定 (default=${task})
    --generation: 実験を何世代行うかを指定 (default=${task})

EOF
)

. ../utils/parse_options.sh

#required args
model=$1

echo $job_no