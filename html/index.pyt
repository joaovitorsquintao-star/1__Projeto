class CalculadoraDeInfluences:

  def __init__(self):
    self.visualizacao = input("Qual e sua visualizaçao por video? ")
    self.preco_por_visualizacao = input("Qual e o preço de cada visualizaçao? ")
    self.nome = input("Qual e o nome do canal? ")
    

  def calcular(self):
      num_visualizacao = float(self.visualizacao) 
      num_preco = float(self.preco_por_visualizacao)
      self.resultado = num_visualizacao * num_preco
      print("="*45)
      print(f"O nome do canal e {self.nome.upper()}")
      print("="*45)
      print(f"A quantidade de dinheiro que voce ira receber e de R$ {self.resultado}")
      print("="*45)


minha_calculadora = CalculadoraDeInfluences()
minha_calculadora.calcular()