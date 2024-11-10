# **Confere Aqui!**
O projeto Confere Aqui! é uma aplicação em Python utilizando a biblioteca Tkinter para criar uma interface gráfica. O objetivo do sistema é permitir que os usuários carreguem uma imagem, visualizem a prévia e, após uma análise de visão computacional com a biblioteca OPENCV, vejam os resultados das questões respondidas, incluindo a quantidade de acertos e erros, com a possibilidade de salvar os resultados em um banco de dados SQLite.

## **Como funciona a leitura:**
1. Leitura e Preprocessamento da Imagem
2. Identificação de Contornos
3. Identificação de Retângulos e Correspondência de Ponto
4. Pré-processamento para Detecção das Respostas
5. Análise das Respostas

**Biblioteca utilizadas:**
- Python 3.x
- Tkinter
- PIL (Pillow)
- SQLite
- Cv2
- numpy
