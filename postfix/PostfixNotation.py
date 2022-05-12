class PostfixNotation:
  priorities = {
    # '!': 1,
    '|': 2,
    '^': 3,
    '&': 4,
  }

  def __init__(self, lexems_file, postfix_file):
    self.lexems_file = lexems_file
    self.postfix_file = postfix_file
    self.find_expression = False
    self.stack = []
    self.results = []
    self.current_expression = ''

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

  def __erase(self):
    for lexem in reversed(self.stack):
      self.current_expression += lexem
    
    self.stack = []
    self.results.append(self.current_expression)
    self.current_expression = ''

  def __process(self, lexem, type):
    if type in ['constant', 'identifier']:
      self.current_expression += lexem
    else:
      if lexem == ')':
        while True:
          lex = self.stack.pop()

          if lex == '(':
            return

          self.current_expression += lex

      if len(self.stack) > 0:
        last = self.stack[-1]

        if last == '!':
          self.current_expression += last
          self.stack.pop()
        elif last not in ['(', ')'] and lexem not in ['(', ')'] and self.priorities[last] > self.priorities[lexem]:
          self.current_expression += last
          self.stack.pop()
          self.stack.append(lexem)
          return

      self.stack.append(lexem)


  def analyze(self):
    for (lexem, type) in self.__find_expressions():
      if lexem == 'end' and type == 'expression::end':
        self.__erase()
        continue

      self.__process(lexem, type)
    print(self.results)

    print('Tests: ------')
    print(self.results[0] == 'b!c0&1|d&1|0&&')
    print(self.results[1] == '10|a!1^&')
    print(self.results[2] == 'b!0^1d&|')
    
