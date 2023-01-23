import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class NeuralNet(nn.Module):
    def __init__(self):
        super (NeuralNet,self).__init__()
        self.linear1 = nn.Linear(15000,6000)
        self.linear2 = nn.Linear(6000,1000)
        self.linear3 = nn.Linear(1000,500)
        self.linear4 = nn.Linear(500,100)
        self.linear5 = nn.Linear(100,64)
        self.linear6 = nn.Linear(64,10)
        self.linear7 = nn.Linear(10,1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
    def forward(self,x):
        x1 = self.relu(self.linear1(x))
        x2 = self.relu(self.linear2(x1))
        x3 = self.relu(self.linear3(x2))

        x4 = self.relu(self.linear4(x3))
        x5 = self.relu(self.linear5(x4))
        x6 = self.relu(self.linear6(x5))
        x7 = self.relu(self.linear7(x6))
        x7= self.sigmoid(x7)

        return x7
