# Projeto Grau A: Heian Shodan com Yanshee

## Finalidade

Este projeto tem como objetivo programar o robô educacional Ubtech Yanshee para executar uma coreografia sequencial inspirada nos movimentos básicos do kata de caratê **Heian Shodan**, adaptando os comandos nativos de movimentação da API para simular posturas de defesa e ataque.

## Ambiente

* **Hardware:** Robô Ubtech Yanshee (equipado com Raspberry Pi e 1GB de RAM).
* **Linguagem:** Python 3.5.3
* **Biblioteca:** `YanAPI` para interface e controle de movimentos.

## Estrutura

O código principal é estruturado da seguinte forma:

1. **Inicialização:** Conexão local com a API do robô utilizando o endereço IP loopback (`127.0.0.1`).
2. **Coreografia (`coreografia_heian_shodan`):** Uma lista contendo tuplas com o nome do comando de movimento e o tempo de pausa (ritmo), dividida em quatro blocos lógicos:
   * **Bloco 1 (Esquerda):** Preparação, giro de 90º, simulação de defesa baixa (`LeftTackle`), avanço e soco direito (`RightHitForward`).
   * **Bloco 2 (Direita):** Giro de 180º, defesa baixa (`RightTackle`), avanço e soco esquerdo (`LeftHitForward`).
   * **Bloco 3 (Frente / Caminho do I):** Sequência alternada de avanços e socos culminando em um golpe finalizador (`Fight_RHit`) com simulação de *KIAI!*.
   * **Bloco 4 (Retorno e Conclusão):** Grande rotação de 270º pelas costas, defesa, avanço, soco final e retorno à posição de repouso (`Reset`).
3. **Loop de Execução:** Executa síncronamente cada movimento via `YanAPI.sync_play_motion`, validando o sucesso da chamada e respeitando os intervalos de pausa configurados.

## Configuração

1. Certifique-se de que o script está sendo executado diretamente no ambiente Python do Raspberry Pi embutido no robô Yanshee, onde a biblioteca `YanAPI` e as dependências de hardware estão disponíveis.
2. Confirme se o IP local (`127.0.0.1`) é o correto para a sua execução interna ou se exige alteração para acesso via rede (*A confirmar*).

## Execução

Para rodar o script no robô, utilize o terminal Python do sistema:

```bash
python nome_do_script.py
```

O robô iniciará na postura de atenção (`Reset` / *Yoi*), processará cada passo da coreografia imprimindo o status no console e retornará ao estado inicial ao término (*Yame*).

## Limites e O Que Falta Confirmar

* **Restrições de Hardware (1GB RAM):** O robô possui recursos limitados de memória e processamento. Deve-se confirmar se a execução síncrona contínua e as pausas curtas (como `0.5` segundos) sobrecarregam o daemon de controle de movimentos ou causam latência (*A confirmar*).
* **Mapeamento de Movimentos:** Os comandos utilizados (ex: `LeftTackle`, `RightHitForward`, `Fight_RHit`) são padrões herdados da versão v1 da API do Yanshee. É necessário testar fisicamente para validar se a correspondência motora reproduz adequadamente a biomecânica esperada do caratê ou se causa instabilidade e quedas (*A confirmar*).
* **Versão da API:** O código especifica explicitamente o parâmetro `version="v1"`. É preciso confirmar se o firmware atual instalado no robô suporta integralmente esta versão sem erros de rejeição de argumentos (*A confirmar*).
