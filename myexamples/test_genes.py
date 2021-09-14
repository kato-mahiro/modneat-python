# The Python standard library import
import sys
import os
import shutil

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# The NEAT-Python library imports
import modneat

# Read config file
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config = modneat.Config(modneat.DefaultGenome, modneat.DefaultReproduction,
                     modneat.DefaultSpeciesSet, modneat.DefaultStagnation, 
                     config_path)

#初期個体群を生成、一つの個体を取得など
# Create the population, which is the top-level object for a NEAT run.
p = modneat.Population(config)

# Add a stdout reporter to show progress in the terminal.
p.add_reporter(modneat.StdOutReporter(True))
stats = modneat.StatisticsReporter()
p.add_reporter(stats)
p.add_reporter(modneat.Checkpointer(5, filename_prefix='out/modneat-checkpoint-'))


### 適当に個体群を生成して, そこから一つのネットワークを取得したい

#pop = modneat.Population(config)
#print(p.population)
#print(p.species)
list(p.population.items()) #ゲノムのリストを取得
#print(list(p.population.items()))
print(len(list(p.population.items()))) #150
print(list(p.population.items())[0])

g = list(p.population.items())[0][1] #個体群の最初の個体の遺伝子を取得

#一つのfeedforwardNetworkの個体をgから生成する
net = modneat.nn.FeedForwardNetwork.create(g, config)