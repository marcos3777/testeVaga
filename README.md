# Aplicação de Estágio - Exercícios em Python

Este projeto faz parte de um processo seletivo para uma vaga de estágio. Nele, foram implementados diversos exercícios em Python, abordando manipulação de strings, cálculos matemáticos, operações com arquivos JSON/XML e conceitos de lógica e estrutura de dados.

## Índice
1. [Exercício 1 - Cálculo da Soma](#exercício-1---cálculo-da-soma)
2. [Exercício 2 - Sequência de Fibonacci](#exercício-2---sequência-de-fibonacci)
3. [Exercício 3 - Faturamento Mensal](#exercício-3---faturamento-mensal)
4. [Exercício 4 - Percentual de Faturamento por Estado](#exercício-4---percentual-de-faturamento-por-estado)
5. [Exercício 5 - Inversão de String](#exercício-5---inversão-de-string)

---

## Exercício 1 - Cálculo da Soma
O primeiro exercício consiste em calcular a soma de números consecutivos utilizando uma estrutura de repetição. O objetivo é determinar a soma após o processamento de um laço `while`, simulando um algoritmo de cálculo sequencial.

### Descrição
- Uma variável `INDICE` é definida como 13.
- A soma é calculada para todos os números de 1 até o valor de `INDICE`.
- A implementação utiliza um laço `while` e exibe o valor final da soma.

---

## Exercício 2 - Sequência de Fibonacci
Este exercício verifica se um número informado pelo usuário pertence à sequência de Fibonacci, utilizando operações matemáticas e laços.

### Descrição
- O programa solicita ao usuário um número e verifica se ele faz parte da sequência de Fibonacci.
- Há verificações para entradas inválidas, como números negativos ou entradas não numéricas. O programa permanece em loop até que o usuário insira "sair".
- A tela é limpa em caso de entrada inválida para proporcionar uma melhor experiência de uso.

---

## Exercício 3 - Faturamento Mensal
Este exercício processa os dados de faturamento diário de uma distribuidora, fornecidos em um arquivo JSON ou XML. O objetivo é calcular o menor e o maior valor de faturamento e determinar o número de dias em que o faturamento foi superior à média mensal.

### Descrição
- Os dados são lidos de um arquivo JSON ou XML.
- Dias com faturamento igual a zero (indicando feriados ou finais de semana) são excluídos do cálculo da média.
- O programa realiza os seguintes cálculos:
  - Menor valor de faturamento do mês.
  - Maior valor de faturamento do mês.
  - Número de dias em que o faturamento diário foi superior à média mensal.

---

## Exercício 4 - Percentual de Faturamento por Estado
O objetivo deste exercício é calcular o percentual de participação no faturamento total de uma distribuidora, detalhado por estado.

### Descrição
- São fornecidos os valores de faturamento para os estados: SP, RJ, MG, ES e "Outros".
- O programa calcula e exibe o percentual de cada estado em relação ao valor total mensal.

---

## Exercício 5 - Inversão de String
O último exercício consiste em inverter os caracteres de uma string fornecida pelo usuário, sem utilizar funções prontas como `reverse`.

### Descrição
- O programa solicita ao usuário que insira uma string e verifica se ela possui mais de um caractere.
- Caso a entrada seja inválida (apenas um caractere ou vazia), o console é limpo e o usuário é solicitado a fornecer uma nova entrada.
- Quando uma entrada válida é fornecida, o programa inverte a string manualmente, utilizando um loop, e exibe o resultado.
