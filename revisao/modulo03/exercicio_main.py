from exercicio_classes_AVIAO  import Aviao
from exercicio_classes_MOTO  import Moto


viajar = Moto(65, 1250, 'Preta', 'manual')


print(viajar)
print('*'*50)


voar = Aviao('Cargueiro', 1000, 5000, 6)

print(voar)
print(f'O modelo deste aviao eh {voar.tipo}')