# Prova---P1---Sistemas-Distribiudos

Nome: Felipe Wodewotsky
RA: ecdc9dcb2d2eeef4fee4

## Problema da empresa

A empresa procura um serviço que calcula o preço final de uma venda após a aplicação de desconto, assim, neste caso, consideramos um cenário que o servidor deve calcular o valor resultante considerando um valor de R$200,00 com 10% de desconto.

## Arquivos

- servidor.py: recebe a chamada RPC e executa o cálculo.
- cliente.py: solicita o cálculo ao servidor e mostra a resposta.

## Resultado do teste

- Resultado do servidor:
&'C:\Program Files\Python313\python.exe' 'c:\Users\aluno\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher' '60637' '--' 'C:\Users\aluno\prova 30.09\Arquivo servidor.py' 
Servidor RPC aguardando solicitações...
127.0.0.1 - - [30/Sep/2026 22:20:04] "POST / HTTP/1.1" 200 -

- Resultado do cliente:
& 'C:\Program Files\Python313\python.exe' 'c:\Users\aluno\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher' '59468' '--' 'C:\Users\aluno\prova 30.09\Arquivo cliente.py' 
Preço final: 180.0

## Explicação

1. O programa foi executado pelo servidor.py, sendo ali onde se encontra o código que detalha o cálculo que será realizado.

2. O cliente solicita a pergunta, sendo ali apresentado quais valores que será utilizado para realizar o cálculo e assim nos retorna o valor calculado pelo servidor.

3. O calculo não seria realizado, visto que o servidor estaria fora do ar e não realizaria o cálculo. Apareceria uma mensagem de erro informado que  "Nenhuma conexão pôde ser feita porque a máquina de destino as recusou ativamente"
Segue código de erro caso o cliente seja executado enquanto o servidor está desligado:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "c:\Users\aluno\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher\__main__.py", line 92, in <module>
    main()
    ~~~~^^
  File "c:\Users\aluno\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher\__main__.py", line 48, in main
    launcher.connect(host, port)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
ConnectionRefusedError: [WinError 10061] Nenhuma conexão pôde ser feita porque a máquina de destino as recusou ativamente
