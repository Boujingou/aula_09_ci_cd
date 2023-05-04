import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    # dados o numero 2 e o numero 5
    primeiro = 2
    segundo = 5

    # calcula a soma
    output = methods.soma(primeiro, segundo)
    
    # entao a soma deve ser 7
    assert output == 7

def test_subtracao():
    # dados o numero 2 e o numero 5
    primeiro = 2
    segundo = 5

    # calcula a subtracao
    output = methods.subtracao(primeiro, segundo)
    
    # entao a subtracao deve ser 7
    assert output == -3
 
def test_multiplicacao():
    # dados o numero 2 e o numero 5
    primeiro = 2
    segundo = 5

    # calcula a multiplicacao
    output = methods.multiplicacao(primeiro, segundo)
    
    # entao a multiplicacao deve ser 7
    assert output == 10
 
def test_divisao():
    # dados o numero 2 e o numero 5
    primeiro = 2
    segundo = 5

    # calcula a divisao
    output = methods.divisao(primeiro, segundo)
    
    # entao a divisao deve ser 7
    assert output == 0.4