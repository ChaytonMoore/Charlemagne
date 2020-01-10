import random
import matplotlib.pyplot as plt
alphabet = "abcdefghijklmnopqrstuvwxyz"
letteridx = ["a.txt","b.txt","c.txt","d.txt","e.txt","f.txt"]
LEARNING = 1.5 #I believe 1.5 is a good number
#A neural network that is designed to be able to recognise images.

#These are the start values for the previous values
previousFitness = 0
previousobjs = [] #Note this is know just a list of values that would be in the positions
#They are only needed for the random backprop

class Node():
    layer = 0
    weights = []
    outputs = []
    values = []
    passon = 0
    letterrep = ""
    


# Create Node Start #######
#There are 84 input nodes
#There have to be 26 output nodes
#There should be 100 nodes per hidden layer
#There will be 5 hidden layers 
objs = [Node() for i in range(610)]

def RBackprop(objs,previousobjs,previousFitness,meanScore,actualScore):
    #This is the type of backprop which is random 
    CHANGENUM = 10 #The number of random numbers needed
    #Here are the calculations for the fitness value
    Fitness = actualScore/meanScore
    if Fitness < previousFitness:
        print("Erronous run, will reset")
        for i in range(0, len(objs)):
            for j in range(0, len(objs[i].weights)):
                objs[i].weights[j] = previousobjs[i][j]
                
    
    if Fitness > previousFitness:
        previousobjs = []
        for i in objs:
            temp = []
            for j in i.weights:
                temp.append(j)
            previousobjs.append(temp)
        previousFitness = Fitness
        Rands = []
        for i in range(0, CHANGENUM):
            Rands.append(random.randint(0, len(objs)-1))
            
        for i in range(0, len(objs)):
            if i in Rands:
                for j in range(0, len(objs[i].weights)):
                    objs[i].weights[j] = random.random()
    
    
    return objs,previousobjs,previousFitness
        
            
    
    

#def rewardFunc():

def backprop(actualL,chosenL,meanScore,actualScore,objs):
    if actualL != chosenL:#Towards the start this is the most likely path
        rewardFunc()
   # else:


        

layer0 = []
layer1 = []
layer2 = []
layer3 = []
layer4 = []
layer5 = []
layer6 = []

#order = [layer0,layer1,layer2,layer3,layer4,layer5]

cont = 0
for i in range(0, 84):
    layer0.append(objs[i])

for i in range(84, 184):
    layer1.append(objs[i])


for i in range(184, 284):
    layer2.append(objs[i])


for i in range(284, 384):
    layer3.append(objs[i])


for i in range(384, 484):
    layer4.append(objs[i])


for i in range(484, 584):
    layer5.append(objs[i])


for i in range(584, 610):
    layer6.append(objs[i])
    
for i in range(0, len(layer6)):
    layer6[i].letterrep = alphabet[cont]
    cont += 1

    

# Create Node End #########

# Set up weights and Ouputs Start #
for i in range(0, len(layer0)):
    layer0[i].outputs = layer1
    
for i in range(0, len(layer1)):
    layer1[i].outputs = layer2
    
for i in range(0, len(layer2)):
    layer2[i].outputs = layer3

for i in range(0, len(layer3)):
    layer3[i].outputs = layer4

for i in range(0, len(layer4)):
    layer4[i].outputs = layer5

for i in range(0, len(layer5)):
    layer5[i].outputs = layer6
    
#outputs create end
    
for i in range(0, len(layer0)):
    for j in range(0, len(layer0[i].outputs)):
        layer0[i].weights.append(random.random())
        
for i in range(0, len(layer1)):
    for j in range(0, len(layer1[i].outputs)):
        layer1[i].weights.append(random.random())
        
for i in range(0, len(layer2)):
    for j in range(0, len(layer2[i].outputs)):
        layer2[i].weights.append(random.random())
        
for i in range(0, len(layer3)):
    for j in range(0, len(layer3[i].outputs)):
        layer3[i].weights.append(random.random())
        
for i in range(0, len(layer4)):
    for j in range(0, len(layer4[i].outputs)):
        layer4[i].weights.append(random.random())
        
for i in range(0, len(layer5)):
    for j in range(0, len(layer5[i].outputs)):
        layer5[i].weights.append(random.random())
        


 #Set up Nodes End #

#Temp data set up, should be removed later
data = []
for i in range(0, 84):
    data.append(random.randint(0,1))
for i in range(0, len(layer0)):
    layer0[i].passon = data[i]
    
timesh = 0
while True:
    inp = input("What do you want to do.")
    if inp == "run":#Will just do it via going from layer to layer
        for i in range(0, len(layer1)):
            for j in layer0:
                layer1[i].values = layer1[i].values + [(j.passon * j.weights[i])]
        layer1[i].passon = sum(layer1[i].values)
    
        for i in range(0, len(layer2)):
                for j in layer1:
                    layer2[i].values = layer2[i].values + [(j.passon * j.weights[i])]
                layer2[i].passon = sum(layer2[i].values)
        
        for i in range(0, len(layer3)):
                for j in layer2:
                    layer3[i].values = layer3[i].values + [(j.passon * j.weights[i])]
                layer3[i].passon = sum(layer3[i].values)
        
        for i in range(0, len(layer4)):
                for j in layer3:
                    layer4[i].values = layer4[i].values + [(j.passon * j.weights[i])]
                layer4[i].passon = sum(layer4[i].values)
            
        for i in range(0, len(layer5)):
                for j in layer4:
                    layer5[i].values = layer5[i].values + [(j.passon * j.weights[i])]
                layer5[i].passon = sum(layer5[i].values)
            
        for i in range(0, len(layer6)):
                for j in layer5:
                    layer6[i].values = layer6[i].values + [(j.passon * j.weights[i])]
                layer6[i].passon = sum(layer6[i].values)

        
    
    if inp == "kill":
        break
        exit()
    
    if inp == "print":
        for i in layer6:
            print(i.passon)
    
    if inp == "change learning":
        print("The learning constant should stay above 1 otherwise it'll learn backwards around 1.5 is fine I think.")
        LEARNING = input("New learning constant")
    
    if inp == "load":
        letterR = random.randint(0, 5)
        file = letteridx[letterR]
        filedata = open(file,"r")
        filedata = filedata.read()
        for i in range(0, len(layer0)):
            layer0[i].passon = int(filedata[i])
        actual = file[0]
        print("loaded",actual)
        
    
    if inp == "determine":
        winner = ""
        wvalue = 0
        y = []
        for i in layer6:
            if i.passon > wvalue:
                wvalue = i.passon
                winner = i.letterrep
            y.append(i.passon)
        
        x = []
        for i in range(0, 26):
            x.append(i)
        ab_split = []
        for i in range(0, 26):
            ab_split.append(alphabet[i])
        tick_label = ab_split
        plt.bar(x, y, tick_label = tick_label, width = 0.6, color = ["red","green"])
        plt.title("output strengths")
        
        plt.show()
        print("the winner is",winner)
        
        #Adds all the output values to a list 
        results = [] 
        for i in layer6:
            results.append(i.passon/wvalue)
        
        mean = sum(results)/len(results)
        
        if winner == actual: #if the AI has picked the correct 
            lpos = alphabet.index(actual)
            CorrectLetter = layer6[lpos].passon
            reward = CorrectLetter / wvalue
            reward = reward / LEARNING
        else:
            #The wvalue is the highest
            lpos = alphabet.index(actual)
            CorrectLetter = layer6[lpos].passon
            reward = CorrectLetter / wvalue
            reward = reward / LEARNING
            print(reward,"reward")
            print("The average was",mean)
           # backprop()
            
    if inp == "backprop": #This function needs the programme to have already been ran etc
        print("Will now perform backpropagation.")
        print("The programme should already have been ran.")
        obj = backprop()
    
    if inp == "rbackprop":
        print("Will now run the Rbackprop.")
        objs,previousobjs,previousFitness = RBackprop(objs,previousobjs,previousFitness,mean,reward)
        
        
    if inp == "RTrain":
        print("Will now perform training using the random backprop.")
        letterperfect = input("Do you want to keep the same letter?(y/n)")
        times = int(input("How many times do you want to train it for."))
        FitnessGraph = []
        maxGraph = []
        for i in range(0, times):
            print(i)
            #First it needs to load a random letter from the possible choices
            if letterperfect != "y" or i == 0:
                
                letterR = random.randint(0, 5)
                file = letteridx[letterR]
                filedata = open(file,"r")
                filedata = filedata.read()
                for i in range(0, len(layer0)):
                    layer0[i].passon = int(filedata[i])
                actual = file[0]
                print("loaded",actual) #Might want to remove this for most runs.
            
            #This is the code that runs the neural network, normally in the run command
            for i in range(0, len(layer1)):
                for j in layer0:
                    layer1[i].values = layer1[i].values + [(j.passon * j.weights[i])]
            layer1[i].passon = sum(layer1[i].values)
        
            for i in range(0, len(layer2)):
                    for j in layer1:
                        layer2[i].values = layer2[i].values + [(j.passon * j.weights[i])]
                    layer2[i].passon = sum(layer2[i].values)
            
            for i in range(0, len(layer3)):
                    for j in layer2:
                        layer3[i].values = layer3[i].values + [(j.passon * j.weights[i])]
                    layer3[i].passon = sum(layer3[i].values)
            
            for i in range(0, len(layer4)):
                    for j in layer3:
                        layer4[i].values = layer4[i].values + [(j.passon * j.weights[i])]
                    layer4[i].passon = sum(layer4[i].values)
                
            for i in range(0, len(layer5)):
                    for j in layer4:
                        layer5[i].values = layer5[i].values + [(j.passon * j.weights[i])]
                    layer5[i].passon = sum(layer5[i].values)
                
            for i in range(0, len(layer6)):
                    for j in layer5:
                        layer6[i].values = layer6[i].values + [(j.passon * j.weights[i])]
                    layer6[i].passon = sum(layer6[i].values)
            
            
            
            #Now the determine part of the code needs to be ran. This version had no graph
            
            winner = ""
            wvalue = 0
            y = []
            for i in layer6:
                if i.passon > wvalue:
                    wvalue = i.passon
                    winner = i.letterrep
                y.append(i.passon)
        
            
            #Adds all the output values to a list 
            results = [] 
            for i in layer6:
                results.append(i.passon/wvalue)
                
        
            mean = sum(results)/len(results)
        
            if winner == actual: #if the AI has picked the correct 
                lpos = alphabet.index(actual)
                CorrectLetter = layer6[lpos].passon
                reward = CorrectLetter / wvalue
                reward = reward / LEARNING
            else:
                #The wvalue is the highest
                lpos = alphabet.index(actual)
                CorrectLetter = layer6[lpos].passon
                reward = CorrectLetter / wvalue
                reward = reward / LEARNING
               # backprop()
            
            
            #Now for the actual back prop function.
            objs,previousobjs,previousFitness = RBackprop(objs,previousobjs,previousFitness,mean,reward)
            FitnessGraph.append(reward/mean)
            maxGraph.append(1/mean)
            #This should be able to perfect the code
        print("Training done.")
        print(FitnessGraph)
        print("It might be a good idea to now see if it will do anything.")
        x = []
        for i in range(0, len(FitnessGraph)):
            x.append(i)
        y = FitnessGraph
        print("x",x)
        print(y)
    
        plt.plot(x, y) 
        plt.plot(x, maxGraph)

        plt.xlabel('Itteration') 

        plt.ylabel('Fitness') 
   
        plt.title('Algorithmic Fitness') 
  
        plt.show()
        
        #Second graph based on distance between lines
        
        differenceScore = []
        for i in range(0, len(y)):
            differenceScore.append(y[i]/FitnessGraph[i])
        