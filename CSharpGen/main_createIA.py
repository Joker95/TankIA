from pylab import *
import matplotlib.pyplot as plt

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb


# A partir d'un réseau fait à la main
learner=gum.BNLearner("log.csv")
learner.useLocalSearchWithTabuList()
bn = learner.learnBN()
gnb.showBN(bn)
