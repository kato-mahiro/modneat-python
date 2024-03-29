"""Uses `pickle` to save and restore populations (and other aspects of the simulation state)."""
from __future__ import print_function
from operator import attrgetter

import os
import gzip
import random
import time
import modneat

try:
    import cPickle as pickle  # pylint: disable=import-error
except ImportError:
    import pickle  # pylint: disable=import-error

from modneat.population import Population
from modneat.reporting import BaseReporter
from modneat import visualize


class Checkpointer(BaseReporter):
    """
    A reporter class that performs checkpointing using `pickle`
    to save and restore populations (and other aspects of the simulation state).
    """

    def __init__(self, savedir, stats, generation_interval=100, time_interval_seconds=300):
        """
        Saves the current state (at the end of a generation) every ``generation_interval`` generations or
        ``time_interval_seconds``, whichever happens first.

        :param str savedir: Name of a directory which store checkpoints and graph
        :param generation_interval: If not None, maximum number of generations between save intervals
        :type generation_interval: int or None
        :param time_interval_seconds: If not None, maximum number of seconds between checkpoint attempts
        :type time_interval_seconds: float or None
        """
        self.savedir = savedir
        self.stats = stats
        self.generation_interval = generation_interval
        self.time_interval_seconds = time_interval_seconds
        self.filename_prefix = self.savedir + '/checkpoints/checkpoint-'

        self.current_generation = None
        self.last_generation_checkpoint = -1
        self.last_time_checkpoint = time.time()

    def start_generation(self, generation):
        self.current_generation = generation

    def post_evaluate(self, config, population, species_set, best):
        checkpoint_due = False

        if self.time_interval_seconds is not None:
            dt = time.time() - self.last_time_checkpoint
            if dt >= self.time_interval_seconds:
                checkpoint_due = True

        if (checkpoint_due is False) and (self.generation_interval is not None):
            dg = self.current_generation - self.last_generation_checkpoint
            if dg >= self.generation_interval:
                checkpoint_due = True

        if checkpoint_due:
            self.save_checkpoint(config, population, species_set, self.current_generation)
            self.last_generation_checkpoint = self.current_generation
            self.last_time_checkpoint = time.time()

    def save_checkpoint(self, config, population, species_set, generation):
        """ Save the current simulation state. """
        filename = '{0}{1}'.format(self.filename_prefix, generation)
        print("Saving checkpoint to {0}".format(filename))

        with gzip.open(filename, 'w', compresslevel=5) as f:
            data = (generation, config, population, species_set, random.getstate())
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

        """Save the png formatted figure of best network toplogy."""
        list_of_genome = list(population.values())
        list_of_genome = sorted(list_of_genome, key=attrgetter('fitness'))
        best_genome = list_of_genome[-1]
        visualize.draw_net(config, best_genome, directory=self.savedir+'/bests', filename='best_{0}'.format(generation), show_disabled=False)

        visualize.plot_stats(self.stats, ylog=False, view=False, filename=os.path.join(self.savedir, 'avg_fitness.png'))
        visualize.plot_species(self.stats, view=False, filename=os.path.join(self.savedir, 'speciation.png'))

    @staticmethod
    def restore_checkpoint(filename):
        """Resumes the simulation from a previous saved point."""
        with gzip.open(filename) as f:
            generation, config, population, species_set, rndstate = pickle.load(f)
            random.setstate(rndstate)
            return Population(config, (population, species_set, generation))
