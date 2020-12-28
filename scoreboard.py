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
