    prob_arrange = numpy.arange(0.55, 1.05, 0.05)
    print(prob_arrange)
[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]  
  
    prob_around = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)
    print(prob_around)
[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]  
  
    probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
    print(probs)
[1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]  