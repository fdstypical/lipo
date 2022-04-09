import re

class Lexical:
  def __init__(self, lexems, input, output):
    self.lexems = lexems
    self.input = input
    self.output = output

    self.lexem = ""
    self.nline = 1
    self.letter = False
    self.digit = False

  def analyze(self):
    while char := self.input.read(1):
      if re.match(r"[a-zA-Z]", char):
        self.lexem += char
        self.letter = True
      elif re.match(r"[0-9]", char):
        self.lexem += char
        self.digit = True
      else:
        if self.letter and not self.digit:
          if self.lexem in self.lexems:
            self.output.write_lexem(self.lexem, self.lexems[self.lexem], self.nline)
          else:
            self.output.write_lexem(self.lexem, "identifier", self.nline)
        elif not self.letter and self.digit:
          self.output.write_lexem(self.lexem, "constant", self.nline)
        else:
          if self.lexem:
            self.output.write_lexem(self.lexem, "0", self.nline)

        self.lexem = ""
        self.letter = self.digit = False

        if char == "\n":
          self.nline += 1
          continue
        if char != " ":
          if char in self.lexems:
            self.output.write_lexem(char, self.lexems[char], self.nline)
          else:
            self.output.write_lexem(char, "0", self.nline)
