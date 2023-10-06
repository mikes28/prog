import random

health= 100
task_list= ["Találkoztál egy nagy, éhes tigrissel", "Átkeltél egy veszélyes folyón, és az áramlat elragadott","Megbotlottél egy csapdában.","Eltévedtél a dzsungelben","Egy mérgező kígyó támadt rád."]
dice=[1,2,3,4,5,6]
lose=8

def boldText(text):
  bold_start = '\033[1m'
  bold_end = '\033[0m'
  return bold_start + str(text) + bold_end

def diceRnd():
   return random.choice(dice)

def completed():
   print("Biztonságban vagy, és elérted az utazásod célját")

def newChallenge():
   global times
   if not task_list:
      completed()
      exit(0)
   else:     
      task=random.choice(task_list)
      task_list.remove(task)
      challenge(task)
      

def diceDrop():
   global health  # indicate that health is a global variable
   
   input("Nyomd meg az entert a dobáshoz!  ")
   dice = diceRnd()
   print(f"A dobásod {dice}")
   if dice == 6:
      print(f"Ügyes vagy, sikerült a kihívást teljesítened!, Életerőd: {boldText(health)}")
      input("Követkető lépéshez nyomd meg az entert!")
      newChallenge()
   while dice != 6:
      if dice == 1:
         health -= lose
         checkIfEnd()
         print(f"Sajnos ez nem volt elég, vesztettél {lose} életerőt, és újra kell dobnod!  Életerőd: {boldText(health)}")
      diceDrop()

def checkIfEnd():
       if health<=0:
         print("Sajnálom, de ez az út számodra véget ért :(")
         exit(0)
       else: return

def challenge(task):
   print(f"{task}, dobj hatost, hogy legyőzd. Ha egyes dobsz, elvesztesz {lose} életerőt. Életerőd: {boldText(health)}")
   diceDrop()

   
def question():
   print(
      '''
      Melyik utat választod?
      1:Hosszú, de biztonságos.
      2:Rövid, de veszélyes
      ''')
   ans=input()
   while ans not in ["1", "2"]:
      ans=input("Érvénytelen válaszlehetőség, kérlek add meg válaszod újra! \n", )
   return ans


def app():
   if (question()=="1"):
      completed()
   else: newChallenge()


if __name__=="__main__":
   app()









   
