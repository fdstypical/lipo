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

input = open("source.txt", "r")
output = LexemsFile("lexems.txt", "w")

lexical = Lexical(lexems, input, output)
lexical.analyze()

input.close()
output.close()

GLOBAL_IDENTS = []

def A(file):
  lexem, type, nline = file.read_lexem()

  if lexem != "Var":
    raise Exception(f"Expected `Var`, got `{lexem}` with type `{type}`", nline)

def B(file):
  lexem, type, nline = file.read_lexem()

  while type == 'identifier':
    GLOBAL_IDENTS.append(lexem)

    lexem, type, nline = file.read_lexem()

    if lexem == ',':
      lexem, type, nline = file.read_lexem()

      if type != 'identifier':
        raise Exception(f"Expected `identifier`, got `{lexem}` with type `{type}`", nline)
    elif lexem == ':':
      break
    else:
      raise Exception(f"Expected `:` or `,`, got `{lexem}` with type `{type}`", nline)

def C(file):
  lexem, type, nline = file.read_lexem()

  if type == 'key_word::type_definition':
    lexem, type, nline = file.read_lexem()

    if lexem != ';':
      raise Exception(f"Expected `;`, got `{lexem}` with type `{type}`", nline)
  else:
    raise Exception(f"Expected lexem with type `key_word::type_definition`, got `{lexem}` with `{type}`", nline)

def D(file):
  lexem, type, nline = file.read_lexem()

  if lexem != 'Begin':
    raise Exception(f"Expected `Begin`, got `{lexem}` with type `{type}`", nline)

  E(file)

def F(file):
  lexem, type, nline = file.read_lexem()

  if lexem == '!':
    lexem, type, nline = file.read_lexem()
  
  if type == 'constant':
    lexem, type, nline = file.read_lexem()

    if lexem != ';':
      raise Exception(f"Expected `constant`, got `{lexem}` with type `{type}`", nline)
  else:
    raise Exception(f"Expected `constant`, got `{lexem}` with type `{type}`", nline)

def E(file):
  lexem, type, nline = file.read_lexem()

  while type == 'identifier':
    if lexem not in GLOBAL_IDENTS:
      raise Exception(f"Identifier `{lexem}` is not declared", nline)

    lexem, type, nline = file.read_lexem()

    if lexem == ':':
      lexem, type, nline = file.read_lexem()

      if lexem == '=':
        F(file)
        lexem, type, nline = file.read_lexem()
        pass
      else:
        raise Exception(f"Expected `=`, got `{lexem}` with type `{type}`", nline)
    else:
      raise Exception(f"Expected `:`, got `{lexem}` with type `{type}`", nline)
  else:
    if lexem != "End":
      raise Exception(f"Expected `End`, got `{lexem}` with type `{type}`", nline)
    else:
      lexem, type, nline = file.read_lexem()

      if lexem != '.':
        raise Exception(f"Expected `.`, got `{lexem}` with type `{type}`", nline)

ll = LinkedList()

ll.add_last(Node(A)) \
  .add_last(Node(B)) \
  .add_last(Node(C)) \
  .add_last(Node(D)) \

lexems_file = LexemsFile("lexems.txt", "r")

syntactical = Syntactical(lexems_file, ll)
syntactical.analyze()

lexems_file.close()