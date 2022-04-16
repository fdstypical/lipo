class LexemsFile:
  def __init__(self, path, type = 'r'):
    self.path = path
    self.type = type
    self.file = open(path, type)
    self.last = self.file.tell()

  def write_lexem(self, lexem, type, nline):
    self.file.write(f"{lexem}\t{type}\t{nline}\n")

  def read_lexem(self, sep = '\t'):
    self.last = self.file.tell()
    lexem, type, nline = self.file.readline().split(sep)
    return (lexem, type, int(nline))

  def back_last(self):
    return self.file.seek(self.last)

  def close(self):
    self.file.close()
