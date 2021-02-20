import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import random
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from datetime import datetime


file= app_files.words
file_content = str(file.get_bytes().decode("utf-8"))
x = file_content.split("\n")

words ={line.strip("\n").strip("\r").strip("'s").lower() for line in x}  # A set.
words = sorted(words)[1:]  # Ignore the empty word at the start of the list.

source_words = []
good_words = []
def filter_soruce_words():
  for w in words:
    if len(w) > 7:
      source_words.append(w)
    if len(w) > 3:
      good_words.append(w)

 

def select_source_word():
  return random.choice(source_words)

def process_words(words):
  check_words(words)
  
  
  
def check_input(words,s_word):
  words_set = set(words.split())
  message = ""
  invalid_words = []
  invalid_letters = set()
  smaller_words = []
  
  # check number of words
  if len(words_set) != 7:
   # message = "You have entered wrong number of words or used duplicates! \n"
    pass
   
  # check if words are in the dictionary
  for w in words_set:
    
    if w not in good_words:
      invalid_words.append(w)

    if len(w) < 4:
      smaller_words.append(w)
        
    source = list(s_word)
    for l in list(w):
      if l in source:
        source.remove(l)
      else:
        invalid_letters.add(l)
    
    
  # add invalid words to the error message
  if len(invalid_words) !=0:
    message = message + "Invalid Words: "
    for w in invalid_words:
      message = message + w + " "
    message = message + "\n"
    
  if len(smaller_words) !=0:
    message = message + "Words that are too short: "
    for w in smaller_words:
      message = message + w + " "
    message = message + "\n"
    
  if len(smaller_words) !=0:
    message = message + "Invalid letters: "
    for l in invalid_letters:
      message = message + l + " "
    message = message + "\n"
  
  # display error message
  if message != "":
    message = message + "\n\n Try Again!"
    alert(message)
    return False
  
  return True
  

def start_timer():
  t = time.time()
  return t

def get_timestamp():
  timestamp = datetime.now()
  timestamp_string = timestamp.strftime("%d/%m/%Y %H:%M:%S")
  return timestamp_string
  