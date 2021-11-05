# Snake Game feito em Python
## *Projeto final da disciplina de APC 2021/1*
##### Ciclo básico de engenharia na Universidade de Brasília, campus Gama

### Notas
- Escolhi python pela rapidez e por ser *cross-platform*, implementar o jogo em C++ e OpenGL demandaria mais tempo

- O desenvolvimento foi feito de maneira mais desacoplada, permitindo mais facilmente modificações e a implementação de features

- É recomendado o uso de virtual env para instalar as bibliotecas
### Recomendações
| Programa | Versão |
| ------ | ------ |
| Python | >= 3.9.x |
| Pip | >= 21.x |

## Executando a aplicação:

Em seu terminal, navegar para o diretório em que os arquivos estão.

Antes de abrir o jogo, execute o comando:
```sh
pip install -r requirements.txt
```
Para abrir o jogo, execute o comando:
```sh
python main.py
```


## Instruções de jogo:

- Usar as setas direcionais para mudar o sentido de movimento da cobrinha
- Comer as frutas que aparecem na tela garantem pontos e aumentam seu tamanho


### TODO:

- Adicionar um contador de pontos na tela
- Adicionar menus de configuração e de inicio de jogo
- Feature para salvar o score em arquivo
- Verificar retrocompatibilidade
- Averiguar a possibilidade de modos de jogo diferentes
