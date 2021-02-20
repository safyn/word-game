import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
from . import game
import anvil.http

@anvil.server.callable
def get_scores():
    return app_tables.scores.search(tables.order_by('score'))
  

@anvil.server.callable
def add_score(the_name,the_score,the_source_word,the_words_entered):
  
  app_tables.scores.add_row(name=the_name,
                            score=the_score,
                            source_word=the_source_word,
                            words_entered=the_words_entered)
  
@anvil.server.callable
def record_log(the_result,the_source_input,the_timestamp, the_user_agent):

  app_tables.logs.add_row(result=the_result,
                          source_input = the_source_input,               
                          timestamp=the_timestamp,
                          ip=anvil.server.context.client.ip,
                          user_agent=the_user_agent)
  
  
@anvil.server.callable
def get_logs():
  return app_tables.logs.search()
                       
  
@anvil.server.http_endpoint('/get-user-agent')
def get_user_agent():
  return {'ua': anvil.server.request.headers['user-agent']}