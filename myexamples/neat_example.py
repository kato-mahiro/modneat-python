import argparse
import sys
import os
import shutil

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# The NEAT-Python library imports
import modneat
# The helper used to visualize experiment results
import task

# The current working directory
local_dir = os.path.dirname(__file__)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--network_type', type=str, help='', default='FeedForwardNetwork')
    parser.add_argument('--genome_type', type=str, help='', default='DefaultGenome')
    parser.add_argument('--config_path', type=str, help='', default='./config/config.ini')
    parser.add_argument('--savedir', type=str, help='', default='./results')
    parser.add_argument('--task', type=str, help='', default='task.xor')

    args = parser.parse_args()
    return args

def run_experiment(config_file):
    """
    Arguments:
        config_file: the path to the file with experiment configuration
    """
    # Load configuration.
    config = modneat.Config(GENOME_TYPE, modneat.DefaultReproduction,
                         modneat.DefaultSpeciesSet, modneat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = modneat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(modneat.StdOutReporter(True))
    p.add_reporter(modneat.FileOutReporter(True, out_dir + '/results.txt'))
    stats = modneat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(modneat.Checkpointer(5, filename_prefix= out_dir + '/checkpoints/checkpoint-'))

    # Run for up to 100 generations.
    best_genome = p.run(TASK.eval_genomes, 100)
    TASK.show_results(best_genome, config, stats, out_dir)


def clean_output():
    if os.path.isdir(out_dir):
        # remove files from previous run
        shutil.rmtree(out_dir)

    # create the output directory
    os.makedirs(out_dir, exist_ok=False)
    os.makedirs(out_dir + '/checkpoints', exist_ok=False)


if __name__ == '__main__':
    # Get args
    args = create_parser()
    NETWORK_TYPE = eval('modneat.nn.' + args.network_type)
    GENOME_TYPE = eval('modneat.' + args.genome_type)
    TASK = eval(args.task + '(network_type = NETWORK_TYPE)')
    CONFIG_PATH = os.path.join(local_dir, args.config_path)

    # The directory to store outputs
    out_dir = os.path.join(local_dir, args.savedir, args.task + '_' + args.network_type)

    # Clean results of previous run if any or init the ouput directory
    clean_output()

    # Run the experiment
    run_experiment(CONFIG_PATH)
