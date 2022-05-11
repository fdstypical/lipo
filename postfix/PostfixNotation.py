class PostfixNotation:
  def __init__(self, lexems_file, postfix_file):
    self.lexems_file = lexems_file
    self.postfix_file = postfix_file
    self.find_expression = False

  def __find_expressions(self):
    while True:
      lexem, type = self.lexems_file.read_lexem()[:2]

      if type == '2':
        lexem, type = self.lexems_file.read_lexem()[:2]

        if type == '4':
          lexem, type = self.lexems_file.read_lexem()[:2]
          self.find_expression = True
      
      if self.find_expression and type == '3':
        self.find_expression = False
        yield ('end', 'expression::end')

      if self.find_expression:
        yield (lexem, type)

      if type == 'key_word::end':
        break

  def analyze(self):
    for (lexem, type) in self.__find_expressions():
      if lexem == 'end' and type == 'expression::end':
        print('erase stack and parse new expression')
        continue

      print(lexem, type)