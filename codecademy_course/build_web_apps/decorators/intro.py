
def decorator(function):
  #*args, **kwargs son necesarios para que el decoraador funcione con parametros
  def wrapper(*args, **kwargs):
    math = "Operacion Metematica"
    function(*args, **kwargs)
  return wrapper

@decorator #evita que se tenga que instanciar el decorador con la funcion
def fun_suma(x, y):
  add = x + y
  print("La suma da: " + str(add))

@decorator #evita que se tenga que instanciar el decorador con la funcion
def fun_resta(x, y):
  sub = x - y
  print("La resta da: " + str(sub))

sumando = decorator(fun_suma)
restando = decorator(fun_resta)

fun_suma(10, 4)
print()
fun_resta(10, 4)

    
    