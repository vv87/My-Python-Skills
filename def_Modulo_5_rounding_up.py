def closest_mod_5(x):
    if x % 5 == 0:
        return(x)
    return(x + 5 - x % 5)
    
'''
 Write the implementation of the function closest_mod_5, 
 which takes an integer x as the only argument and returns the smallest integer y, such that:

 y is greater than or equal to x
 y is divisible by 5
 The format of what is expected of you as an answer:

 def closest_mod_5 (x):
  if x% 5 == 0:
  return x
  return "I don't know :("
  
  
  Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента 
  целое число x и возвращающую самое маленькое целое число y, такое что:

 y больше или равно x
 y делится нацело на 5
 Формат того, что ожидается от вас в качестве ответа:

 def closest_mod_5(x):
     f x % 5 == 0:
         return x
     return "I don't know :(  '''
