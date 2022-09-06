E1.  
    prob_arrange = numpy.arange(0.55, 1.05, 0.05)
    print(prob_arrange)
[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]  
'0.55' if the starting number of the array. '1.05' is the ending number of the array. To be noticed, the generated array only contains the staring number and does not contain the ending number. '0.05' is the step length, which means the differences between each two neighboring numbers.  
  
    prob_around = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)
    print(prob_around)
[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]  
The `numpy.around()` function is used to round numbers in an array to the given number of digits in `decimal = n`. However, in this case, because the number in the array is has either two decimals or one, the `numpy.around()` function will not change the values in the array.   
  
    probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
    print(probs)
[1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]  
The useage of [::-1] is to reverse the given iterable variable while not to change the data type of the variable.  
  
E2.  
The power means how many tests led to the rejection of the null hypothesis that the coin is a non-biased coin. When the toss number increases, the simulatoin result will be closer to the theoretical results, which leads to higher difference between simulation results and non-biased coin hypothesis. Thus, higher occurance of rejection will be seen, giving higher power. Similar to this, increasing of probabilities of head-turnings makes the simulation further away from non-biased coin hypothesis, which makes it easier for hypothesis test to give rejection. Therefore, in conclusion, the power goes higher to 1 when toss number increases or the coin becomes more biased.  
  
E3.  
a)  
The paper mainly focus on testing Mendel's Separation Law (detecting transmission distortion, TD) in human by analysing sperm single cell sequencing data. Before the whole genome sequencing of huamn sperm came out, one way to test Mendel's Separation Law in human is pedigree-based analyzation. However, the small size of human families can limit the detection of TD. Gamete sequencing was also available, but contrained by the technical challenges and costs, previous gamete sequencing could only work on small number of sperms. Thus, the emergence of whole genome sperm sequencing makes it possible to analyse TD in human.  
However, the existing data has relatively low coverage. And this paper tried to develop a method package to analyze TD in such data, which also provides accessible tools for related studies in future.  
  
b)  
Both figures are studying the power changing under changing of probabilities and number of trials (tosses or sperm number).  
In S13, the heatmap has more rows and columns. And its y-axis starts from 0.5, which means it contains the simulation of evenly-separated sperms, while coin-toss simulation does not include non-biased coin results.  
  
The `prob_heads` corresponds to transmission rate.  
  
The `n_toss` corresponds to number of sperms.  
  
A binomial distribution is a discrete probability distribution with parameters n and p. It records the distribution of the number of successes in a sequence of n independent experiments, each asking a yes–no question, and each with its own Boolean-valued outcome: success (with probability p) or failure (with probability q = 1 − p).  
In coin-toss simulation, n is the number of tosses, head-or-tail is the yes-no question and the probability of head_turnings is p while q=1-p is for tails.  
In the simulation in paper, n is the number of sequenced sperms, whether an allele can go in to a specified daughter gamete cell is the yes-no question, and the probability of the allele going into a specified daughter gamete is p here, which is also called transmission rate.