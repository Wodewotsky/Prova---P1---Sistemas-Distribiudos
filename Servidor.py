from xmlrpc.server import SimpleXMLRPCServer

def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

servidor = SimpleXMLRPCServer(("localhost", 8001))

servidor.register_function(
    calcular_desconto,
    "calcular_desconto"
)

print("Servidor RPC aguardando solicitações...")

servidor.serve_forever()
