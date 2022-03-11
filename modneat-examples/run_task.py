import argparse
import sys
import os
import shutil

# The NEAT-Python library imports
import modneat
# The helper used to visualize experiment results
import task

# The current working directory
local_dir = os.path.dirname(__file__)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--network', type=str, help='', default='FeedForwardNetwork')
    parser.add_argument('--config', type=str, help='', default='./configs/default_genome.ini')
    parser.add_argument('--savedir', type=str, help='', default='./results')
    parser.add_argument('--task', type=str, help='', default='task.xor')
    parser.add_argument('--generation', type=int, help='', default=100)
    parser.add_argument('--run_id', type=int, help='', default=0)

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

    # Run for up to args.generations.
    best_genome = p.run(TASK.eval_genomes, GENERATION)
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
    NETWORK_TYPE = eval('modneat.nn.' + args.network)
    GENOME_TYPE = NETWORK_TYPE.genome_type()
    TASK = eval(args.task + '(network_type = NETWORK_TYPE)')
    CONFIG_PATH = os.path.join(local_dir, args.config)
    GENERATION = args.generation

    # The directory to store outputs
    out_dir = os.path.join(local_dir, args.savedir, args.task + '_' + args.network + '_' + str(args.run_id))

    # Clean results of previous run if any or init the ouput directory
    clean_output()

    # Run the experiment
    run_experiment(CONFIG_PATH)
