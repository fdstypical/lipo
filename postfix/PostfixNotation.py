class PostfixNotation:
  priorities = {
    '=': 0,
    '!': 1,
    '|': 2,
    '^': 3,
    '&': 4,
  }

  def __init__(self, lexems_file, postfix_file):
    self.lexems_file = lexems_file
    self.postfix_file = postfix_file
    self.exp_finded = False
    self.stack = []

  def __find_idents(self):
    while True:
      lexem, type = self.lexems_file.read_lexem()[:2]

      if type == 'identifier':
        self.postfix_file.write(f"{lexem} ")

      if type == 'key_word::type_definition':
        self.postfix_file.write(f"{lexem}\n")
        break
  
  def __find_expressions(self):
    while True:
      lexem, type = self.lexems_file.read_lexem()[:2]

      if type == 'identifier':
        self.exp_finded = True

      if type == 'key_word::end':
        self.exp_finded = False
        break

      if self.exp_finded and type == '3':
        self.__erase()

      if self.exp_finded:
        self.__postfix(lexem, type)
  
  def __pop_brackets(self):
    while True:
      lex = self.stack.pop()

      if lex == '(':
        break

      self.postfix_file.write(f"{lex}")

  def __check_stack(self, lexem):
    last = self.stack[-1]

    if last == '!':
      self.postfix_file.write(f"{last}")
      self.stack.pop()
      last = self.stack[-1]

    while last not in ['(', ')', '!'] and lexem not in ['(', ')', '!'] and self.priorities[last] > self.priorities[lexem]:
      self.postfix_file.write(f"{last}")
      self.stack.pop()
      last = self.stack[-1]

  def __erase(self):
    for lexem in reversed(self.stack):
      self.postfix_file.write(f"{lexem}")
    
    self.stack = []
    self.exp_finded = False
    self.postfix_file.write('\n')

  def __postfix(self, lexem, type):
    if type in ['constant', 'identifier']:
      self.postfix_file.write(f"{lexem}")
    else:
      if type == '8::end':
        self.__pop_brackets()
        return

      if len(self.stack) > 0:
        self.__check_stack(lexem)

      if type != '2':
        self.stack.append(lexem)

  def analyze(self):
    self.__find_idents()
    self.__find_expressions()
