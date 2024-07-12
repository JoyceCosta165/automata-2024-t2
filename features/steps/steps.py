from behave import given, when, then
from src.automata import load_automata, process, convert_to_dfa

# Passos já definidos anteriormente
@given('um arquivo automata "{filename}"')
def step_given_automata_file(context, filename):
    context.automata_file = filename

@when('eu carrego o autômato')
def step_when_load_automata(context):
    try:
        context.automata = load_automata(context.automata_file)
        context.load_successful = True
    except Exception:
        context.load_successful = False

@then('deve retornar um autômato válido')
def step_then_valid_automata(context):
    assert context.automata is not None

@then('deve retornar "INVÁLIDA"')
def step_then_invalid_automata(context):
    assert not context.load_successful

@when('eu processo a palavra "{word}"')
def step_when_process_word(context, word):
    context.result = process(context.automata, list(word))

@then('o resultado deve ser "{expected_result}"')
def step_then_expected_result(context, expected_result):
    assert context.result['result'] == expected_result

@when('eu converto para DFA')
def step_when_convert_to_dfa(context):
    context.dfa = convert_to_dfa(context.automata)

@then('deve retornar um DFA válido')
def step_then_valid_dfa(context):
    assert context.dfa is not None

# Novos passos sugeridos
@given(u'a descrição de um automato finito')
def step_impl(context):
    # Aqui você pode definir a lógica para criar a descrição de um autômato finito
    context.automata_description = """
    a b
    q0 q1 q2 q3
    q0 q3
    q0
    q0 a q1
    q0 b q2
    q1 a q0
    q1 b q3
    q2 a q3
    q2 b q0
    q3 a q1
    q3 b q2
    """

@when(u'eu peço a validação das palavras')
def step_impl(context):
    # Implemente a lógica para validar palavras com base na descrição do autômato
    automata = load_automata(context.automata_description)
    context.results = process(automata, ["a", "b"])

@then(u'nenhum erro ocorre na criação do automato')
def step_impl(context):
    # Verifique se o autômato foi criado sem erros
    try:
        load_automata(context.automata_description)
    except Exception:
        assert False, "Erro ocorreu na criação do autômato"

@then(u'o resultado obtido é')
def step_impl(context):
    # Verifique o resultado obtido
    expected_result = {"result": "REJEITA"}
    assert context.results == expected_result

@when(u'eu crio o automato')
def step_impl(context):
    # Implemente a lógica para criar o autômato
    try:
        context.automata = load_automata(context.automata_description)
    except Exception:
        context.automata = None

@then(u'um erro ocorre na criação do automato')
def step_impl(context):
    # Verifique se ocorreu um erro na criação do autômato
    assert context.automata is None
