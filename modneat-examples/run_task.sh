#!/bin/bash

set -euo pipefail

python -m modneat.run \
--network FeedForwardNetwork \
--task cartpole_v0 \
--savedir HOGE \
--config ./configs/default_genome.ini