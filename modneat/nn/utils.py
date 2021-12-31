def weight_change(self, input_node, output_node, value):
    """ Add value to connection weight between input_node and output_node. """
    node_loop_counter = -1

    for _output_node, *_, links in self.node_evals:
        node_loop_counter += 1
        connection_loop_counter = -1

        for _input_node, *_ in links:
            connection_loop_counter += 1
            if(input_node == _input_node and output_node == _output_node):
                listed_node_and_weight = list(self.node_evals[node_loop_counter][-1][connection_loop_counter])
                listed_node_and_weight[1] += value
                self.node_evals[node_loop_counter][-1][connection_loop_counter] = tuple(listed_node_and_weight)
                #print('ノード{},{}の間の重みを {} だけ変更しました'.format(input_node, output_node, value))
            else:
                pass
