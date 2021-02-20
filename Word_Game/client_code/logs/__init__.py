from ._anvil_designer import logsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class logs(logsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_log_panel.items = anvil.server.call('get_logs')