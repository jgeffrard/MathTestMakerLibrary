import dotProducts # "import questiongenerator.dotProducts as dp" does not work; I get ModuleNotFoundError; i am running Python 3.7.4

dot = dotProducts.DotProducts()
ret = dot.getQuestion(list(dot.getQuestionNames())[0], 1, 1 )
print(ret)