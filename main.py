# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from operator import add,sub

#Reads file from path and returns the content
def get_file_contents(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content

# parse the first n lines in str and returns dict count of rejected, pos, and neg samples
def parse(str):
    count_dict = {
        "rej": 0,
        "pos": 0,
        "neg":0,
    }
    probs = []
    n_accepted = []
    samples = str.splitlines()
    for i in samples:
        if i == '-1':
            count_dict['rej'] += 1
        elif i == '1':
            count_dict['pos'] += 1
        elif i == '2':
            count_dict['neg'] += 1

        if (count_dict['pos'] + count_dict['neg']) > 0:
            probs.append(count_dict['pos']/(count_dict['pos'] + count_dict['neg']))
        else:
            probs.append(-1) #invalid probs (0 accepted samples)

        n_accepted.append(count_dict['pos'] + count_dict['neg'])
    return probs, n_accepted

def computeProb(dict):
    return dict['pos']/ (dict['pos'] + dict['neg'])

def graph(x, y, n_accepted = None):
    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
    ax.set_xscale('log')
    ax.plot(x, y, label='x')  # Plot some data on the Axes.
    ax.set_xlabel('Number of samples')  # Add an x-label to the Axes.
    ax.set_ylabel('P(+r|+s, +w)')  # Add a y-label to the Axes.
    ax.set_title('P(+r|+s, +w) vs Number of Samples')  # Add a title to the Axes.

    if n_accepted is not None:
        eps = [math.log(0.025)/(-2* n) for n in n_accepted]
        y_plus = list(map(add, y, eps))
        y_min = list(map(sub, y, eps))

        ax.plot(x, y_plus, label = 'x + ep')
        ax.plot(x, y_min, label = 'x - ep')

    plt.legend()
    plt.show()

def parse2(str):
    weight_dict = {
        't':0,
        'f':0
    }
    probs=[]
    lines = str.splitlines()
    for line in lines:
        split = line.split(',')
        if split[0] == 'True':
            weight_dict['t'] += float(split[1])
        elif split[0] == 'False':
            weight_dict['f'] += float(split[1])

        probs.append(weight_dict['t'] /(weight_dict['t'] + weight_dict['f']))

    return probs

def main():
    content = get_file_contents('data/rs_1.csv')
    probs, n_accepted = parse(content)
    y = [val for val in probs if val != -1] #remove invalid probs
    n_accepted_graph = [val for val in n_accepted if val != 0] #remove invalid n_accepted for graph
    # print(probs[0:20])
    # print(y[0:20])
    # print(len(probs))
    # # print(len(y))
    # print(n_accepted[0:10])
    # print(len(n_accepted))
    # print(n_accepted_graph[0:10])
    # print(len(n_accepted_graph))

    #part a.i/b.iii
    x = np.arange((100000 - len(y)) + 1,100001) #from 2 to 100000
    # print(x)
    # print(len(x))
    assert (len(x) == len(y))
    graph(x,y, n_accepted_graph)

    #part a.ii
    given_N = [21424, 40927, 71205, 100000]
    find_prob = [probs[n - 1] for n in given_N]
    print('prob of given Ns: ',find_prob)

    #part b.ii
    accepted_samples = n_accepted[99999] #n of accepted when N=100000
    print('# of accepted_samples at N = 100000: ', accepted_samples)
    ep = math.log(0.025)/(-2*accepted_samples)
    print('epsilon at N = 100000: ', ep)

    #part c.i
    content2 = get_file_contents('data/lw_1.csv')
    probs2 = parse2(content2)
    # print (probs2[0:10])
    # print(len(probs2))
    x2 = np.arange(1,100001) #from 1 to 100000
    assert (len(x2) == len(probs2))
    graph(x2, probs2)

    #partc.ii
    given_N2 = [3563, 48450, 92851, 100000]
    find_prob2 = [probs2[n - 1] for n in given_N2]
    print('prob of given Ns for second file: ',find_prob2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
