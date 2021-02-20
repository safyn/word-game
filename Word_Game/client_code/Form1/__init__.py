from ._anvil_designer import Form1Template
import anvil.tables as tables
from anvil.tables import app_tables
import anvil.server
from .. import game
import time
from ..top10 import top10
from ..logs import logs
from anvil import *
import anvil.http
from datetime import datetime



class Form1(Form1Template):
  t = float(0)
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    game.filter_soruce_words()
    self.source_word_label.text = ""

   

  def play_button_click(self, **event_args):
    words = self.words_text_box.text
    
    source_word = self.source_word_label.text
    score =0
    score = round((time.time() - t),2)
    user_agent = anvil.http.request(anvil.server.get_api_origin() + '/get-user-agent', json=True)['ua']
    
    # if correct answer
    if game.check_input(words,source_word):

      anvil.server.call('add_score',
                        self.name_box.text,
                        score,
                        self.source_word_label.text,
                        self.words_text_box.text)
      
      # record sucessfull try
      anvil.server.call('record_log',
                        "SUCCESS",
                        self.source_word_label.text + ": " + self.words_text_box.text,
                        game.get_timestamp(),
                        user_agent)
      
      # Open result window
      alert(content=top10(),
            title="Top Scores\n\n Amazing! Your score is:" + str(score) + " seconds",
            large=True)
      
    # answer isnt correct
    else:
      # record unsuccesfull try 
      anvil.server.call('record_log',
                        "ERROR",
                        self.source_word_label.text + ": " + self.words_text_box.text,
                        game.get_timestamp(),
                        user_agent)
    

  # Top score window
  def top_scores_button_click(self, **event_args):
   alert(content=top10(), title="Top Scores",large=True)

  # Reroll the word: restarts the timer
  def reroll_word_button_click(self, **event_args):
        self.source_word_label.text = game.select_source_word()
        global t
        t = game.start_timer()

   # display log window    
  def logs_button_click(self, **event_args):
    alert(content=logs(),title="LOGS",large=True)
   


