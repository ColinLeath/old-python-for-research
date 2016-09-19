#Purpose is to test probability.
#three conditions. we're interested in the range of the distributions (how likely are we to get extreme values?)
#
conditions=['strategy + fixed','random + fixed','random + random','strategy + random']
DATAFIXED = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
maxsessions=1000
f = open('prtest.csv','w')
import random
for condition in conditions:
    print condition
    f.write('%s,' % condition)  #label row with condition name
    for n in range(maxsessions):
        countOfTrialsCorrect = 0
        #we need to initialize variables:
        if condition[-5:]=='fixed':
            print 'shuffling datafixed'
            random.shuffle(DATAFIXED)

        for trial in DATAFIXED:
            
            #1. get choice:
            if condition[:8] =='strategy':
                myChoice = 1
            elif condition[:6] =='random':
                myChoice = random.choice([1,0])
            else:
                print 'choice: error! no condition matched!'

            #2. get answer:
            if condition[-5:] == 'fixed':
                answer = trial
            elif condition[-6:] == 'random':
                answer = random.choice([1,0])
            else:
                print 'answer: error! no condition matched!'

            #3. are we correct?
            if myChoice == answer:
                countOfTrialsCorrect += 1
        #    DataFixed = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
        
        #we need to tally results as decimal fractions:
        decimalFractionCorrect = float(countOfTrialsCorrect)/float(len(DATAFIXED))
        #1: run a sequence of trials
            # for each trial, decide if correct value or not
            # total correct values and divide by DataFixed.count()
            # record this in a file.
            # output will look like
            #       .33,.56,.47 .... maxtrials
            # summary stats: for each we'll want the standard deviation.
            #we'll read data into excel as rows then transpose probably:
            #condition name: .33, .56, etc.
            # o.k.!
       
        f.write('%0.3f,' % decimalFractionCorrect)
    f.write('\n')
        #record output:
         
f.close()
