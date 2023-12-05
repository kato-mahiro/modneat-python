#!bin/bash

rm -rf ./results/*

#実行
time python -m modneat.run --task xor --config ./configs/bool_global.ini --savedir ./results/bool_global && \
time python -m modneat.run --task xor --config ./configs/float_local.ini --savedir ./results/float_local && \
#マルチコア
time python -m modneat.run --task xor --config ./configs/bool_global.ini --num_workers 4