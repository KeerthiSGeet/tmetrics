import savingandrestoring
import matplotlib.pyplot as plt 
import sys

if __name__ == '__main__':
    # service.py executed as script
    # do something
    positive=0
    negative=0
    with open('demofile.txt') as f:
       for line in f:
           if(savingandrestoring.use_neural_network(line) == '1'):
              positive = positive+1
           else:
              negative = negative+1

       print('Total negative = ' + str(negative))
       print('Total positive = ' + str(positive))
       import pandas as pd 

    labels = 'Negative Tweets', 'Positive Tweets'
    sizes = [negative, positive]
    colors = ['gold', 'yellowgreen']
    explode = (0.1, 0.1)  # explode 1st slice
 
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
    plt.axis('equal')
    plt.show()
