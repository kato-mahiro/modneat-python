import copy
import math
from modneat.graphs import feed_forward_layers
from modneat.genome import ExHebbGenome, ModExHebbGenome
from modneat.nn import FeedForward
from modneat.nn.utils import weight_change

class ModFeedForward(FeedForward):
    def __init__(self, inputs, outputs, node_evals, global_params, boolian_modulation):
        super().__init__(inputs, outputs, node_evals)
        self.values = dict((key, 0.0) for key in inputs + outputs)
        self.modulate_values = dict((key, 0.0) for key in inputs + outputs)
        self.modulated_values = dict((key, 0.0) for key in inputs + outputs)
        self.global_params = global_params
        self.boolian_modulation = boolian_modulation
    
    @staticmethod
    def genome_type():
        return ModExHebbGenome

    def assert_type(self):
        #a, b, c, d, etaをglobalに設定するか、localに設定するかに関するassrsion
        pass

    def activate(self, inputs, is_update = True):
        if len(self.input_nodes) != len(inputs):
            raise RuntimeError("Expected {0:n} inputs, got {1:n}".format(len(self.input_nodes), len(inputs)))

        for k, v in zip(self.input_nodes, inputs):
            self.values[k] = v

        for node, modulatory_ratio, act_func, agg_func, bias, response, links in self.node_evals:
            node_inputs = []
            for i, w in links:
                node_inputs.append(self.values[i] * w)
            s = agg_func(node_inputs)

            assert modulatory_ratio >= 0.0 and modulatory_ratio <= 1.0, "ERROR:modulatory_ratio must be between 0.0 and 1.0"

            if(self.boolian_modulation):
                if(modulatory_ratio > 0.5):
                    self.values[node] = 0.0
                    self.modulate_values[node] = act_func(bias + response * s)
                else:
                    self.values[node] = act_func(bias + response * s)
                    self.modulate_values[node] = 0.0
            else:
                self.values[node] = act_func(bias + response * s) * (1.0 - modulatory_ratio)
                self.modulate_values[node] = act_func(bias + response * s) * modulatory_ratio

        # Caliculate modulated_values of each node
        for node, modulatory_ratio, act_func, agg_func, bias, response, links in self.node_evals:
            self.modulated_values[node] = self.global_params['m_d']
            for i, w in links:
                self.modulated_values[node] += self.modulate_values[i] * w

        if(is_update):
            for node, modulatory_ratio, act_func, agg_func, bias, response, links in self.node_evals:
                for i, w in links:
                    #Soltoggioの設定に基づいて重みを更新
                    update_val = math.tanh (self.modulated_values[node] / 2.0) * \
                                self.global_params['eta'] * \
                                (
                                    self.global_params['a'] * self.values[i] * self.values[node] + \
                                    self.global_params['b'] * self.values[i] + \
                                    self.global_params['c'] * self.values[node] + \
                                    self.global_params['d'] \
                                )
                    weight_change(self, i, node, update_val)

        return [self.values[i] for i in self.output_nodes]

    @staticmethod
    def create(genome, config):
        """ Receives a genome and returns its phenotype (a FeedForwardNetwork). """

        # Gather expressed connections.
        connections = [cg.key for cg in genome.connections.values() if cg.enabled]

        layers = feed_forward_layers(config.genome_config.input_keys, config.genome_config.output_keys, connections)
        node_evals = []
        for layer in layers:
            for node in layer:
                inputs = []
                node_expr = [] # currently unused
                for conn_key in connections:
                    inode, onode = conn_key
                    if onode == node:
                        cg = genome.connections[conn_key]
                        inputs.append((inode, cg.weight))
                        node_expr.append("v[{}] * {:.7e}".format(inode, cg.weight))

                ng = genome.nodes[node]
                aggregation_function = config.genome_config.aggregation_function_defs.get(ng.aggregation)
                activation_function = config.genome_config.activation_defs.get(ng.activation)
                node_evals.append((node, ng.modulatory_ratio, activation_function, aggregation_function, ng.bias, ng.response, inputs))

        global_params = genome.global_params[0].__dict__

        return ModFeedForward(config.genome_config.input_keys, config.genome_config.output_keys, node_evals, global_params, config.boolian_modulation)