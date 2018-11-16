import json
import random

def read_json():
   with open('test.json', 'r') as f:
      quest_dict = json.load(f)
   return quest_dict   

def get_question(dictionary):
   dict_size = len(dictionary)
   return dictionary[random.randint(0,dict_size-1)]

def get_options(answer, dictionary):
   dict_size = len(dictionary)
   options = []
   options.append(answer)
   while(len(options) < 5):
      opt = dictionary[random.randint(0,dict_size-1)]["Answer"]
      if opt not in options:
         options.append(opt)
   return options

if __name__ == '__main__':
   qdict = read_json()   
   while(True):
      item = get_question(qdict)
      question = item['Question']
      answer = item['Answer']
      options = get_options(answer, qdict)
      random.shuffle(options)
      print("Select from one of these options")
      count = 0
      for o in options:
         print(str(count)+". "+ o)
         count += 1
      count = 0
      print("\n Here is your case")
      something = input(question + " ").lower()
      try:
         result = options[int(something)]
      except TypeError:
         if(something == "exit"):
            break
         continue
      if(result == answer):
         print("\n very good \n")
      else:
         print("\n Wrong, the answer is " + answer + "\n")

  
