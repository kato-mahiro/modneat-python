from matplotlib.pyplot import hist
from modneat import visualize
import os
import copy
import random

class xor:
    # The XOR inputs and expected corresponding outputs for fitness evaluation
    def __init__(self, network_type):
        self.network_type = network_type
        self.xor_inputs  = [(1.0, 1.0), (1.0, 0.0), (0.0, 1.0), (0.0, 0.0)]
        self.xor_outputs = [   (0.0,),     (1.0,),     (1.0,),     (0.0,)]

    def eval_fitness(self, net):
        """
        Arguments:
            net: The feed-forward neural network generated from genome
        Returns:
            The fitness score - the higher score the means the better 
            fit organism. Maximal score: 16.0
        """
        net.reset()
        history = []
        error_sum = 0.0
        history.append(copy.deepcopy(net.__dict__))

        for xi, xo in zip(self.xor_inputs, self.xor_outputs):
            output = net.activate(xi)
            history.append(copy.deepcopy(net.__dict__))
            error_sum += abs(output[0] - xo[0])
        # Calculate amplified fitness
        fitness = (4 - error_sum) ** 2
        return fitness, history

    def eval_genomes(self, genomes, config):
        """
        Arguments:
            genomes: The list of genomes from population in the 
                    current generation
            config: The configuration settings with algorithm
                    hyper-parameters
        """
        for genome_id, genome in genomes:
            genome.fitness = 4.0
            net = self.network_type.create(genome, config)
            genome.fitness, genome.history = self.eval_fitness(net)
    
    def show_results(self, best_genome, config, stats, out_dir):
        # Display the best genome among generations.
        print('\n ************************* Finish evolution *************************  \n')
        print('\nBest genome:\n{!s}'.format(best_genome))

        # Show output of the most fit genome against training data.
        print('\nOutput:')
        net = self.network_type.create(best_genome, config)
        for xi, xo in zip(self.xor_inputs, self.xor_outputs):
            output = net.activate(xi)
            print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))

        # Check if the best genome is an adequate XOR solver
        best_genome_fitness, best_genome_history = self.eval_fitness(net)
        if best_genome_fitness > config.fitness_threshold:
            print("\n\nSUCCESS: The XOR problem solver found!!!")
        else:
            print("\n\nFAILURE: Failed to find XOR problem solver!!!")

        # Visualize the experiment results
        node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
        visualize.draw_net(config, best_genome, False, node_names=node_names, directory=out_dir)
        visualize.plot_stats(stats, ylog=False, view=False, filename=os.path.join(out_dir, 'avg_fitness.png'))
        visualize.plot_species(stats, view=False, filename=os.path.join(out_dir, 'speciation.png'))

class non_static(xor):
    # 同じ入力に対して異なる出力を返す必要があるタスク(一番単純, フィードバック入力なし)
    def __init__(self, network_type):
        self.network_type = network_type
        self.xor_inputs  = [(1.0, 1.0), (1.0, 1.0), (1.0, 1.0), (1.0, 1.0)]
        #self.xor_outputs = [   (1.0,),     (0.33,),     (-0.33,),     (-1.0,)]
        self.xor_outputs = [   (0.5,),     (-0.5,),     (0.5,),     (-0.5,)]

class test_learning:
    #学習能力が適切に機能しているか、進化するかを検証するためのタスク
    def __init__(self, network_type):
        self.network_type = network_type
    
    def reset_task(self):
        self.initial_target = random.uniform(0.2, 0.7)
        self.target = self.initial_target
        self.rate_of_change = random.uniform(0.2, 0.2)
        self.clamp_max, self.clamp_min = 1.0, -1.0
        self.fitness = 0.0

    def eval_fitness(self, net):
        """
        Arguments:
            net: The feed-forward neural network generated from genome
        Returns:
            The fitness score - the higher score the means the better 
            fit organism. Maximal score: 16.0
        """
        history = []
        history.append(copy.deepcopy(net.__dict__))
        fitness_list = []
        for trial_n in range(10):
            self.reset_task()
            net.reset()
            for step_n in range(10):
                output = net.activate([1.0, 0.0], is_update=False) #activate_input, previous_output, feedback_input
                diff = output[0] - self.target
                self.fitness -= abs(diff)
                net.activate([0.0, diff], is_update=True)
                history.append(copy.deepcopy(net.__dict__))

                self.target += self.rate_of_change
                if(self.target > self.clamp_max):
                    self.target = self.clamp_max
                    self.rate_of_change *= -1.0
                elif(self.target < self.clamp_min):
                    self.target = self.clamp_min
                    self.rate_of_change *= -1.0
            fitness_list.append(self.fitness)

        return min(fitness_list), history

    def eval_genomes(self, genomes, config):
        """
        Arguments:
            genomes: The list of genomes from population in the 
                    current generation
            config: The configuration settings with algorithm
                    hyper-parameters
        """
        for genome_id, genome in genomes:
            genome.fitness = 0.0
            net = self.network_type.create(genome, config)
            genome.fitness, genome.history = self.eval_fitness(net)
    
    def eval_single_genome(self, genome, config):
        genome.fitness = 0.0
        net = self.network_type.create(genome, config)
        genome.fitness, genome.history = self.eval_fitness(net)
        return genome.fitness, genome.history
    
    def show_results(self, best_genome, config, stats, out_dir):
        # Display the best genome among generations.
        print('\n ************************* Finish evolution *************************  \n')
        print('\nBest genome:\n{!s}'.format(best_genome))

        # Show output of the most fit genome against training data.
        print('\nOutput:')
        net = self.network_type.create(best_genome, config)
        for xi, xo in zip(self.xor_inputs, self.xor_outputs):
            output = net.activate(xi)
            print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))

        # Check if the best genome is an adequate XOR solver
        best_genome_fitness, best_genome_history = self.eval_fitness(net)
        if best_genome_fitness > config.fitness_threshold:
            print("\n\nSUCCESS: The XOR problem solver found!!!")
        else:
            print("\n\nFAILURE: Failed to find XOR problem solver!!!")

        # Visualize the experiment results
        node_names = {-1:'Activate', -2: 'Feedback', 0:'Output'}
        visualize.draw_net(config, best_genome, False, node_names=node_names, directory=out_dir)
        visualize.plot_stats(stats, ylog=False, view=False, filename=os.path.join(out_dir, 'avg_fitness.png'))
        visualize.plot_species(stats, view=False, filename=os.path.join(out_dir, 'speciation.png'))