#!/bin/bash

set -euo pipefail

model='FeedForwardNetwork'
config='./configs/default_genome.ini'
task='task.xor'
job_no=1
generation=10
savedir='./results'

help_message=$(cat << EOF
Usage: $0 [options]

Options:
    --model: 実験に用いるモデルを指定 (default=${model})
    --config: モデル用の設定ファイルを指定 (default=${config})
    --task: モデルに課すタスクを指定 (default=${task})
    --job_no: 並列実行数を指定 (default=${task})
    --generation: 実験を何世代行うかを指定 (default=${task})
    --savedir: 実験結果を保存するディレクトリ (default=${savedir})
EOF
)

. ../utils/parse_options.sh

