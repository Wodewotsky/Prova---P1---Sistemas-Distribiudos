from xmlrpc.client import ServerProxy

servidor = ServerProxy("http://localhost:8001/")

resultado = servidor.calcular_desconto(200, 10)

print("Preço final:", resultado)

