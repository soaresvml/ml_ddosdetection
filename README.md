
# Planejamento – Oficina Maker Preparação e Análise de Dados
### Grupo 23 – Pedro Henrique Coelho e Vinicius dos Santos Soares
## Objetivo do projeto
Propor, implementar e validar uma solução especificamente para tratar os ataques de rede do tipo DoS/DDoS.
## Fases do projeto
    1. Planejamento
    2. Coleta de dados
    3. Preparação e análise de dados
    4. Modelagem e treinamento
    5. Geração de alertas
    6. Integração
### FASE 2 – Coleta de Dados
Responsável: Pedro Henrique Coelho
Apoio: Vinicius dos Santos Soares
Objetivo: Carregar os arquivos PCAP para um ambiente Python.
Tecnologias: Python 3.8, Anaconda.
Biblioteca Python: DPKT ou outro.
Data de entrega: 31/03
Entrega: Arquivo PCAP carregado como dataset em um ambiente Python.
### FASE 3 – Preparação e Análise de Dados
Responsável: Vinicius dos Santos Soares 
Apoio: Pedro Henrique Coelho 
Objetivo: Determinar os campos relevantes do dataset carregado e gerar bases de teste e treinamento para mineração de dados.
Tecnologias: Jupyter Notebook.
Biblioteca Python: DPKT, scikit-learn, pandas, outros.
Data de entrega: 28/04
Entrega: Bases pré-processadas para mineração de dados (código fontes gerados, relatório técnico, dicionário de dados e base de treinamento).
### FASE 4 – Modelagem e treinamento
Responsável: Pedro Henrique Coelho
Apoio: Vinicius dos Santos Soares
Objetivo: Testar e definir algoritmo de aprendizagem de máquina, através de testes de aprendizagem no Weka.
Tecnologias: Weka.
Data de entrega: 19/05
Entrega: Relatório de execução de testes de aprendizagem de máquina.
### FASE 5 – Geração de alertas
Responsável: Vinicius dos Santos Soares 
Apoio: Pedro Henrique Coelho 
Objetivo: Validação da classificação das medições, gerando alerta com os capôs Data/hora, IP origem, IP destino e tipo de ataque detectado.
Tecnologias: Kali Linux para submeter um ataque DoS (arquivo PCAP), integrar algoritmo de aprendizagem de máquina a um ambiente Python para avaliar o algoritmo, ou fazê-lo diretamente no Weka.
Data de entrega: 02/06
Entrega: Relatório técnico.
### FASE 6 – Integração
Responsável: Pedro Henrique Coelho
Apoio: Vinicius dos Santos Soares
Objetivo: Documentar todas as etapas realizadas.
Data de entrega: 09/06
Entrega: Relatório final
