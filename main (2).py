class player :
  def play(self):
     print("The player is playing cricket")  

class Batsman(player):
  def play(self):
     print("The batsman is batting")

class Bowling(player):
  def play(self):
      print("The bowler is bowling")
batsman=Batsman()
bowler=Bowling () 
batsman.play() 
bowler.play()