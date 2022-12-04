# Ilhas

*Questão 1784 | Beecrowd*  
*[Link para o problema](https://www.beecrowd.com.br/repository/UOJ_2784.html)*

### **Descrição**

Os moradores das Ilhas Brasileiras Ocidentais (IBO) são assíduos jogadores do mais recente jogo online, Magos e Guerreiros. Tão competitivas se tornaram as partidas de Magos e Guerreiros na IBO, que a empresa criadora do jogo decidiu instalar em uma das ilhas um servidor dedicado apenas aos jogadores da IBO.

Entretanto, a empresa sabe que, se os jogadores acharem que o novo servidor é injusto, eles irão parar de jogar Magos e Guerreiros, gerando incontáveis perdas. Para avaliar se o novo servidor é justo, os jogadores vão comparar o desempenho do jogo na ilha que tem a conexão mais rápida e o desempenho na ilha que tem a conexão mais lenta com o novo servidor. Se a diferença de desempenho for muito grande, os residentes da ilha mais distante se sentirão injustiçados e abandonarão o jogo.

A conexão de internet da IBO funciona através de um sistema de cabos de fibra ótica. Pares de ilhas são conectados por cabos, e cada cabo toma um certo tempo (chamado de ping) para comunicar informação entre as duas partes. Quando duas ilhas se comunicam através de uma série de cabos (portanto, através de ilhas intermediárias), o ping entre elas é a soma dos pings de cada cabo no caminho. A rede da IBO foi implementada por ótimos programadores e, portanto, um par de ilhas sempre se comunica através do caminho com menor ping possível.

Dada a configuração da rede da IBO e a ilha em que a empresa deseja instalar o novo servidor, determine a diferença entre os pings da ilha com menor e maior pings até o servidor.

### **Entrada**

A primeira linha contém N (2 ≤ N ≤ 1000) e M (N − 1 ≤ M ≤ 105), o número de ilhas e o número de cabos de fibra ótica, respectivamente. As ilhas são numeradas de 1 a N. Cada uma das M linhas seguintes contém três inteiros Ui (1 ≤ Ui ≤ N), Vi (1 ≤ Vi ≤ N) e Pi (1 ≤ Pi ≤ 1000) e descreve um cabo entre as ilhas Ui e Vi com ping Pi (note que cabos transmitem informação em ambas as direções). Finalmente, a última linha contém um inteiro S (1 ≤ S ≤ N), o número da ilha em que o servidor será instalado.

Cada par de ilhas é conectado por no máximo um cabo de fibra ótica, e nenhum cabo conecta uma ilha a si mesma. É garantido que qualquer ilha consegue se comunicar com qualquer outra através de algum caminho de cabos de fibra ótica.

### **Saída**

Seu programa deve produzir um inteiro representando a diferença entre o ping da ilha com maior ping até o servidor, e o da ilha com menor ping até o servidor. Note que a ilha em que o servidor se encontra não é considerada no cálculo do menor ping.


| **Exemplo de Entrada** | **Exemplo de Saída**|
|-------|--------|
|4 5<br>2 1 5<br>1 3 4<br>2 3 6<br>4 2 8<br>3 4 12<br>1<br>|9<br>|
|6 11<br>1 2 3<br>6 1 9<br>2 6 10<br>2 3 8<br>5 3 3<br>4 3 2<br>2 4 12<br>6 4 1<br>4 5 9<br>1 5 16<br>5 6 5<br>5<br>|11<br>|

### Resultado


