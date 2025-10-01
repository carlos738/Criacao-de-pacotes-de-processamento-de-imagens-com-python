# Criacao-de-pacotes-de-processamento-de-imagens-com-python

# Calculadora Python 📐

Este projeto é uma calculadora simples com operações básicas: soma, subtração, multiplicação e divisão.

## Funcionalidades

- Soma: `somar(a, b)`
- Subtração: `subtrair(a, b)`
- Multiplicação: `multiplicar(a, b)`
- Divisão: `dividir(a, b)`

## Instalação

```bash
pip install calculadora


USO:
from calculadora import somar, dividir

print(somar(10, 5))  # 15
print(dividir(10, 2))  # 5.0

INTERFACE GRÁFICA:
python -m calculadora.gui


TESTES
python -m unittest discover tests

EMPACOTAMENTO:
python setup.py sdist bdist_wheel
twine upload dist/*


10-VERSIONAMENTO COM GIT (OPCIONAL)

git init
git add .
git commit -m "Versão inicial"
git remote add origin https://github.com/seuusuario/simplecalc.git
git push -u origin master




📌 OBSERVAÇÕES FINAIS

    Atualize a versão no SETUP.PY
    USE README.MD para a descrição no pypi
    teste totalment antes de publicar
    para testes de publicação, user tespypy:https://test.pypi.org