class Syntactical():
  def __init__(self, lexems_file, syntactical_graph):
    self.lexems = lexems_file
    self.syntactical_graph = syntactical_graph

  def __read_lexem(self, sep = "\t"):
    return self.lexems.readline().split(sep)

  def analyze(self):
    for node in self.syntactical_graph.iterate():
      node.data(self.lexems)

# try:
#   lexem, type, nline = self.__read_lexem()
    
#   if lexem == "Var":
#     lexem, type, nline = self.__read_lexem()

#     while type == 'identifier':
#       lexem, type, nline = self.__read_lexem()

#       if lexem == ',':
#         lexem, type, nline = self.__read_lexem()

#         if type != 'identifier':
#           print('error')
#           break

#         continue
#       elif lexem == ":":
#         break
#       else:
#         print('error 1')
      
#     lexem, type, nline = self.__read_lexem()
#     if lexem == "Logical":
#       lexem, type, nline = self.__read_lexem()

#       if lexem == ";":
#         print('success!')
#     else:
#       print('error 2')
#   else:
#     print('error! 3')
# except:
#   print('end!')
