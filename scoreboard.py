from datetime import datetime

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
      # keyvalue = {workout.usuario: int(workout.repeticao) * int(workout.serie)} 
      # print(workout.usuario, keyvalue)
      keyvalue = {}
      keyvalue[str(workout.usuario)] = int(workout.repeticao) * int(workout.serie)

      if (workout.nome not in self.scores):
        self.scores[workout.nome] = [keyvalue]
      else:
        self.scores[workout.nome].append(keyvalue)

    def status(self, query):
      print(self.scores)
      return self.scores[query]
