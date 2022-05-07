GLOBAL_IDENTS = []

def A(file):
  lexem, type, nline = file.read_lexem()

  if type != "key_word":
    raise Exception(f"Expected `Var`, got `{lexem}` with type `{type}`", nline)

def B(file):
  lexem, type, nline = file.read_lexem()

  while type == 'identifier': # todo: use type == '1' in condition
    GLOBAL_IDENTS.append(lexem)
    lexem, type, nline = file.read_lexem()

    if type == '1':
      lexem, type, nline = file.read_lexem()

      if type != 'identifier':
        raise Exception(f"Expected `identifier`, got `{lexem}` with type `{type}`", nline)
    elif type == '2':
      break
    else:
      raise Exception(f"Expected `:` or `,`, got `{lexem}` with type `{type}`", nline)

def C(file):
  lexem, type, nline = file.read_lexem()

  if type == 'key_word::type_definition':
    lexem, type, nline = file.read_lexem()

    if type != '3':
      raise Exception(f"Expected `;`, got `{lexem}` with type `{type}`", nline)
  else:
    raise Exception(f"Expected lexem with type `key_word::type_definition`, got `{lexem}` with `{type}`", nline)

def D(file):
  lexem, type, nline = file.read_lexem()

  if type != 'key_word::start':
    raise Exception(f"Expected `Begin`, got `{lexem}` with type `{type}`", nline)

  E(file)

def F(file):
  lexem, type, nline = file.read_lexem()

  if type == '6':
    lexem, type, nline = file.read_lexem()
    G(file, lexem, type, nline)
  else:
    G(file, lexem, type, nline)

def G(file, lexem, type, nline):
  if type == '8::start':
    F(file)

    lexem, type, nline = file.read_lexem()

    if type != '8::end':
      raise Exception(f"Excpected `)`, got `{lexem}` with type `{type}`", nline)
    else:
      lexem, type, nline = file.read_lexem()
      
      if type == '5':
        F(file)
      elif type == '8::end':
        file.back_last()
      elif type != '3':
        raise Exception(f"Expected `;`, got `{lexem} with type `{type}``", nline)
  else:
    if type in ['identifier', 'constant']:
      lexem, type, nline = file.read_lexem()

      if type == '5':
        F(file)
      elif type == '8::end':
        file.back_last()
      elif type != '3':
        raise Exception(f"Expected `;`, got `{lexem} with type `{type}``", nline)
    else:
      raise Exception(f"Expected `identifier` or `constant`, got `{lexem}` with type `{type}`", nline)

def E(file):
  lexem, type, nline = file.read_lexem()

  while type == 'identifier':
    if lexem not in GLOBAL_IDENTS:
      raise Exception(f"Identifier `{lexem}` is not declared", nline)

    lexem, type, nline = file.read_lexem()

    if type == '2':
      lexem, type, nline = file.read_lexem()

      if type == '4':
        F(file)
        lexem, type, nline = file.read_lexem()
        pass
      else:
        raise Exception(f"Expected `=`, got `{lexem}` with type `{type}`", nline)
    else:
      raise Exception(f"Expected `:`, got `{lexem}` with type `{type}`", nline)
  else:
    if type != "key_word::end":
      raise Exception(f"Expected `End`, got `{lexem}` with type `{type}`", nline)
    else:
      lexem, type, nline = file.read_lexem()

      if type != '7':
        raise Exception(f"Expected `.`, got `{lexem}` with type `{type}`", nline)
