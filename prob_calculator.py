import copy
import random
# Consider using the modules imported above.

class Hat: 
  def __init__(self, **balls):
    #print(balls)
    self.contents=[]
    for key, value in balls.items():
      for i in range(value):
        self.contents.append(key)  
    #print(self.contents)
  def draw(self, number):
    #random.seed()
    drawlist=[]
    if(number>len(self.contents)):
      return self.contents     
      #self.copycontents=copy.deepcopy(self.contents)
    for i in range(number):      
      #print(random.random())
      index=int(random.random()*len(self.contents))
      #print(index)
      drawlist.append(self.contents.pop(index))
    drawlist.sort()
    return drawlist


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
 
  prob=0
  prob_c=2
  for i in range(prob_c):
    #print(hat.contents, expected_balls, num_balls_drawn, num_experiments)
    count=0
    if(num_experiments<=0):
      return "invalid number experiments entered"
    for ex in range(num_experiments):
      copyhat=copy.deepcopy(hat)
      copyballs=copy.deepcopy(expected_balls)
      result = copyhat.draw(num_balls_drawn)
      for item in result:
        if(item in copyballs):
          copyballs[item]-=1
          if(copyballs[item]==0):
            del copyballs[item]
      if(len(copyballs)==0)   :
        count+=1
      #print("result: ",result,"\n","item:",item,"balls: ",copyballs, count)  
    probability=count/num_experiments 
    prob+=probability
    print(prob, probability)
  avr_prob=prob/prob_c
  print("avrg=",avr_prob)
  return avr_prob