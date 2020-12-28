from datetime import datetime
from exercicio import Exercicio

class Scoreboard:
    def __init__(self):
        self.date = datetime.date(datetime.now())
        self.scores = dict()
    
    def __checkDate(self):
      if self.date != datetime.date(datetime.now()):
        self.scores.clear()
        self.date = datetime.date(datetime.now())
    


    def add(self, workout):
      self.__checkDate()
      keyvalue = {workout.usuario : workout.repeticao} 

      if (workout.nome not in self.scores):
        self.scores[workout.nome] = [keyvalue]
      else:
        self.scores[workout.nome].append(keyvalue)

    def status(self):
      return self.scores




wkteste = Exercicio('abdominal', 30, 'definitelynotsam')

test = Scoreboard()
test.add(wkteste)

outro = Exercicio('abdominal', 20, 'definitelynotsam')
test.add(outro)

outro2 = Exercicio('flexao', 20, 'definitelynotsam')
test.add(outro2)

print(test.status())