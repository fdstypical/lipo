from lexical.lexical import Lexical
from syntactical.syntactical import Syntactical
from postfix.PostfixNotation import PostfixNotation
from CodeGenarator import CodeGenerator
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

if __name__ == '__main__':
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

  lexems_file = LexemsFile("lexems.txt", "r")
  postfix_file = open("postfix.txt", "w")

  postfix = PostfixNotation(lexems_file, postfix_file)
  postfix.analyze()

  lexems_file.close()
  postfix_file.close()

  postfix_file = open('postfix.txt', 'r')
  result_file = open('result.txt', 'w')

  code_gen = CodeGenerator(postfix_file, result_file, lexems)
  code_gen.run()

  postfix_file.close()
  result_file.close()
  