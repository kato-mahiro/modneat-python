import modneat
NETWORK_TYPE = modneat.nn.FeedForwardNetwork

class xor:
    # The XOR inputs and expected corresponding outputs for fitness evaluation
    def __init__(self):
        self.xor_inputs  = [(1.0, 1.0), (1.0, 0.0), (0.0, 1.0), (0.0, 0.0)]
        self.xor_outputs = [   (0.0,),     (1.0,),     (1.0,),     (0.0,)]

    def eval_fitness(self, net):
        """
        Evaluates fitness of the genome that was used to generate 
        provided net
        Arguments:
            net: The feed-forward neural network generated from genome
        Returns:
            The fitness score - the higher score the means the better 
            fit organism. Maximal score: 16.0
        """
        error_sum = 0.0
        for xi, xo in zip(self.xor_inputs, self.xor_outputs):
            output = net.activate(xi)
            error_sum += abs(output[0] - xo[0])
        # Calculate amplified fitness
        fitness = (4 - error_sum) ** 2
        return fitness

    def eval_genomes(self, genomes, config):
        """
        The function to evaluate the fitness of each genome in 
        the genomes list. 
        The provided configuration is used to create feed-forward 
        neural network from each genome and after that created
        the neural network evaluated in its ability to solve
        XOR problem. As a result of this function execution, the
        the fitness score of each genome updated to the newly
        evaluated one.
        Arguments:
            genomes: The list of genomes from population in the 
                    current generation
            config: The configuration settings with algorithm
                    hyper-parameters
        """
        for genome_id, genome in genomes:
            genome.fitness = 4.0
            net = NETWORK_TYPE.create(genome, config)
            genome.fitness = self.eval_fitness(net)