class Syntactical():
  def __init__(self, lexems_file, syntactical_graph):
    self.lexems = lexems_file
    self.syntactical_graph = syntactical_graph

  def __read_lexem(self, sep = "\t"):
    return self.lexems.readline().split(sep)

  def analyze(self):
    try:
      for node in self.syntactical_graph.iterate():
        node.data(self.lexems)
    except ValueError as error:
      (message, ) = error.args
      print(f"Error!\nMessage: {message}\nThe file may have ended before all expected lexems have been read")
    except Exception as error:
      message, line = error.args
      print(f"Error!\nMessage: {message}\nAt line: {line}")
