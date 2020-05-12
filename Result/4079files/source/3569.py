#!/usr/bin/python3
"""
Geschafen im februar 12, 2019
Verfasst von Friederich Fluss
"""
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv1d(15, 10, 3)
        self.conv2 = nn.Conv1d(10, 10, 5)
        self.fc1 = nn.Linear(50, 100)
        self.fc2 = nn.Linear(100, 30)
        self.fc3 = nn.Linear(30, 20)

    def forward(self, x):
        x = F.max_pool1d(F.relu(self.conv1(x)), 3)
        x = F.max_pool1d(F.relu(self.conv2(x)), 5)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

if __name__ == '__main__':
    net = Net()
    print(net)
    """
    create the trainset
    create the testset
    clarify the classes

    """
    import torch.optim as optim
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    """
    train the network
    test the network using testset
    summary
    training on GPU
    """
