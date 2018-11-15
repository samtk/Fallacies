import json
import random

def read_json():
   with open('test.json', 'r') as f:
      quest_dict = json.load(f)
   return quest_dict   

def get_question(dictionary):
   dict_size = len(dictionary)
   return dictionary[random.randint(0,dict_size-1)]

if __name__ == '__main__':
   qdict = read_json()   
   while(True):
      item = get_question(qdict)
      question = item['Question']
      answer = item['Answer']
      something = input(question)
      if(something == "exit"):
         break
      if(something == answer):
         print("very good")

  
