import os
from pathlib import Path
import modneat
from modneat import visualize

local_dir = os.path.join(str(Path().resolve()))
out_dir = str(os.path.join(local_dir, 'out'))

"""
This script make assersions about global genes and 
related functions (crossover, mutation, get_distance).
"""
# 設定ファイルを読み込み
config_path = os.path.join(local_dir, 'default_genome.ini')
config = modneat.Config(modneat.ExampleGlobalGenome, modneat.DefaultReproduction,
                     modneat.DefaultSpeciesSet, modneat.DefaultStagnation, 
                     config_path)

#初期個体群を生成、一つの個体を取得など
p = modneat.Population(config)

# Add a stdout reporter to show progress in the terminal.
p.add_reporter(modneat.StdOutReporter(True))
stats = modneat.StatisticsReporter()
p.add_reporter(stats)
p.add_reporter(modneat.Checkpointer(5, filename_prefix='out/neat-checkpoint-'))

### 適当に個体群を生成して, そこから一つのゲノムやネットワークを取得する
print(p)
g1 = list(p.population.items())[0][1] #個体群の最初の個体の遺伝子を取得
g2 = list(p.population.items())[1][1] #個体群の最初の個体の遺伝子を取得
assert(g1.global_params[0].example_string) #グローバルパラメータにアクセス
assert(g1.global_params[0].example_float) #グローバルパラメータにアクセス
assert(g1.global_params[0].example_bool is not None) #グローバルパラメータにアクセス
print(g1.global_params[0].__dict__)
print("=========================\n")
try:
    assert(g1.global_params[1].example)
    print("このprint文は実行されない")
except:
    pass

print(g1)
print('=======================\n')
print(g2)

print(type(config))

print(g1.distance(g2, config.genome_config))

#一つのfeedforwardNetworkの個体をgから生成する
net = modneat.nn.FeedForwardNetwork.create(g1, config)