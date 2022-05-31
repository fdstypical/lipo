import re

class CodeGenerator:
  comands = {
    'const': 'LIT',
    'ident': 'LOAD',
    '=': 'STO',
    '&': 'AND',
    '|': 'OR',
    '^': 'XOR',
    '!': 'NOT',
  }

  def __init__(self, postfix_file, result_file, lexems):
    self.postfix_file = postfix_file
    self.result_file = result_file
    self.lexems = lexems
    self.first_line = False

  def __is_const(self, lexem):
    return re.match(r"[0-9]", lexem)

  def __is_ident(self, lexem):
    return re.match(r"[a-zA-Z]", lexem)    

  def __expression(self, line):
    for lexem in line[1:]:
      if lexem == '\n':
        continue
      
      if lexem in self.comands:
        if lexem == '=':
          self.result_file.write(f"{self.comands[lexem]} {line[0]}\n")
        elif lexem == '!':
          self.result_file.write(f"{self.comands[lexem]}\n")
        else:
          self.result_file.write(f"{self.comands[lexem]}\n")
      else:
        if self.__is_const(lexem):
          self.result_file.write(f"{self.comands['const']} {lexem}\n")
        elif self.__is_ident(lexem):
          self.result_file.write(f"{self.comands['ident']} {lexem}\n")

  def run(self):
    while line := self.postfix_file.readline():
      if self.first_line:
        self.__expression(line)

      self.first_line = True