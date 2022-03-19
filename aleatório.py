import random
#exibindo um número aleatório
i = random.random()
print(i)
#exibindo um número aleatório através de uma seed (será sempre o mesmo)
random.seed(10)
print(random.random())