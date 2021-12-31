def weight_change(net, input_node, output_node, value):
    """
     Add value to connection weight between input_node and output_node.
     この実装は、
     - net.node_evalsの最初の要素が、output先ノードのIDであること
     - net.node_evalsの各要素の最後が、(入力元ノードID, 重み) 
     となっていることを仮定しています。
    """

    node_loop_counter = -1

    for _output_node, *_, links in net.node_evals:
        node_loop_counter += 1
        connection_loop_counter = -1

        for _input_node, *_ in links:
            connection_loop_counter += 1
            if(input_node == _input_node and output_node == _output_node):
                listed_node_and_weight = list(net.node_evals[node_loop_counter][-1][connection_loop_counter])
                listed_node_and_weight[1] += value
                net.node_evals[node_loop_counter][-1][connection_loop_counter] = tuple(listed_node_and_weight)
                #print('ノード{},{}の間の重みを {} だけ変更しました'.format(input_node, output_node, value))
            else:
                pass
