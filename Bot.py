from Think import *

#name = "network_1"
#n = Think2(name, 2, 2, 3, 2)
#n.weights_randomize()
#n.bias_randomize()
#n.print_network()
#n.network_load()
#n.print_network()
#n.network_save()

class Bot:

    def __init__(self,name, **kwargs):

        score = 0 if 'score' not in kwargs else kwargs['score']
        inputNodes = 3 if 'inputNodes' not in kwargs else kwargs['inputNodes']
        hiddenLayer = 1 if 'hiddenLayer' not in kwargs else kwargs['hiddenLayer']
        hiddenNodes = 4 if 'hiddenNodes' not in kwargs else kwargs['hiddenNodes']
        outputNodes = 2 if 'outputNodes' not in kwargs else kwargs['outputNodes']

        n = Think2(name, inputNodes, hiddenLayer, hiddenNodes, outputNodes)

        n.weights_randomize()
        n.bias_randomize()
        n.network_save()
        #n.network_load()
        n.print_network()
        #n.set_input_layer([[0.12], [0.56], [0.89], [0.534], [0.323]], True)
        #n.print_network()

    #for i in range():
    # file_write(name + "_Nodes.txt", n.N)
    # file_write(name + "_Weight.txt", n.W)
    # file_write(name + "_Bias.txt", n.B)
    # n.network_save()


testBot = Bot("test1")
