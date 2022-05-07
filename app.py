from lexical.lexical import Lexical
from syntactical.syntactical import Syntactical
from general.models import Node, LinkedList
from general.LexemsFile import LexemsFile
from general.rules import A, B, C, D

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
  '|': '5',
  '^': '5',
  '!': '6',
  '.': '7',
  '(': '8::start',
  ')': '8::end',
}

input = open("source.txt", "r")
output = LexemsFile("lexems.txt", "w")

lexical = Lexical(lexems, input, output)
lexical.analyze()

input.close()
output.close()

ll = LinkedList()

ll.add_last(Node(A)) \
  .add_last(Node(B)) \
  .add_last(Node(C)) \
  .add_last(Node(D)) \

lexems_file = LexemsFile("lexems.txt", "r")

syntactical = Syntactical(lexems_file, ll)
syntactical.analyze()

lexems_file.close()