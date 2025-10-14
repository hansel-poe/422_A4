# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

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
        "neg":0
    }
    probs = []
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
    return probs, count_dict

def computeProb(dict):
    return dict['pos']/ (dict['pos'] + dict['neg'])

def graph(x, y):
    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
    ax.set_xscale('log')
    ax.plot(x, y, label='')  # Plot some data on the Axes.
    # ax.xaxis.set_major_locator(ticker.FixedLocator([21424, 40927, 71205, 100000]))
    # ax.xaxis.set_major_formatter(ticker.FixedFormatter([21424, 40927, 71205, 100000]))
    # ax.xaxis.set_minor_locator(ticker.NullLocator())
    ax.set_xlabel('Number of samples')  # Add an x-label to the Axes.
    ax.set_ylabel('P(+r|+s, +w)')  # Add a y-label to the Axes.
    ax.set_title('P(+r|+s, +w) vs Number of Samples')  # Add a title to the Axes.
    plt.show()


# def plot_confidence_bounds():


def main():
    content = get_file_contents('./rs_1.csv')
    probs, count_dict = parse(content)
    y = [val for val in probs if val != -1] #remove invalid probs
    # print(probs[0:20])
    # print(y[0:20])
    # print(len(probs))
    # print(len(y))

    #part a.i
    x = np.arange((100000 - len(y)) + 1,100001) #from 2 to 100000
    # print(x)
    # print(len(x))
    assert (len(x) == len(y))
    graph(x,y)

    #part a.ii
    given_N = [21424, 40927, 71205, 100000]
    find_prob = [probs[n - 1] for n in given_N]
    print('prob of given Ns: ',find_prob)

    #part b.ii
    assert (count_dict['rej'] + count_dict['pos']+ count_dict['neg'] == 100000)
    accepted_samples = count_dict['pos'] + count_dict['neg']
    print('# of accepted_samples at N = 100000: ', accepted_samples)
    ep = math.log(0.025)/(-2*accepted_samples)
    print('epsilon at N = 100000: ', ep)

    #part c.i





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
