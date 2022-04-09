from lexical.lexical import Lexical
from syntactical.syntactical import Syntactical
from general.models import Node, LinkedList
from general.LexemsFile import LexemsFile

lexems = {
  'Var': 'key_word',
  'Logical': 'key_word::type_definition',
  'Begin': 'key_word::start',
  'End': 'key_word::end',
  ',': '1',
  ':': '2',
  ';': '3',
  '=': '4',
  '&': '5',
  '|': '6',
  '!': '7',
  '.': '8',
  '(': '9::start',
  ')': '9::end',
}

input = open("test.txt", "r")
output = LexemsFile("lexems.txt", "w")

lexical = Lexical(lexems, input, output)
lexical.analyze()

input.close()
output.close()

def Root(file):
  A(file)
  B(file)
  C(file)

def A(file):
  lexem, type, nline = file.read_lexem()

  if lexem != "Var":
    raise Exception('unknow lexem', nline)

def B(file):
  lexem, type, nline = file.read_lexem()

  while type == 'identifier':
    lexem, type, nline = file.read_lexem()

    if lexem == ',':
      lexem, type, nline = file.read_lexem()

      if type != 'identifier':
        raise Exception('asf', nline)
    elif lexem == ':':
      break
    else:
      raise Exception('gasg', nline)

def C(file):
  lexem, type, nline = file.read_lexem()

  if type == 'key_word::type_definition':
    lexem, type, nline = file.read_lexem()

    if lexem != ';':
      raise Exception('bla-bla', nline)
  else:
    raise Exception('bla-bla-2', nline)


ll = LinkedList()

# ll.add_last(Node(A)) \
#   .add_last(Node(B)) \
#   .add_last(Node(C))

ll.add_last(Node(Root))

lexems_file = LexemsFile("lexems.txt", "r")

syntactical = Syntactical(lexems_file, ll)
syntactical.analyze()

lexems_file.close()