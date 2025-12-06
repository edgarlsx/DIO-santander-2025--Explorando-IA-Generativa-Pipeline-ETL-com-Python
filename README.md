# ETL de Clientes Bancários – Santander Dev Week Inspired

Projeto de **ETL (Extract, Transform, Load)** inspirado no domínio da API da  
[Santander Dev Week 2023](https://github.com/digitalinnovationone/santander-dev-week-2023-api).

O objetivo é:

- Ler dados **brutos** de usuários, contas, cartões, features e notícias;
- Realizar **joins e agregações**;
- Criar **métricas derivadas** (score de engajamento, segmentação por limite de cartão, taxa de utilização da conta);
- Salvar uma **tabela única enriquecida de usuários** em `data/processed/users_enriched.csv`.

---

## 🧱 Estrutura do Projeto

```bash
.
├── data
│   ├── raw
│   │   ├── users.csv
│   │   ├── accounts.csv
│   │   ├── cards.csv
│   │   ├── features.csv
│   │   └── news.csv
│   └── processed
│       └── users_enriched.csv
├── src
│   ├── etl
│   │   ├── __init__.py
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   └── main_etl.py
├── requirements.txt
└── README.md

```

===========================================
## 🚀 Como Rodar o Projeto

### 1. Clonar o repositório

git clone https://github.com/seu-usuario/etl-clientes-banco.git
cd etl-clientes-banco

---

### 2. Criar e ativar um ambiente virtual (opcional, recomendado)

Windows:
python -m venv .venv
.venv\Scripts\activate

Linux / MacOS:
python -m venv .venv
source .venv/bin/activate

---

### 3. Instalar as dependências

pip install -r requirements.txt

yaml
Copiar código

---

### 4. Estrutura esperada dos dados de entrada

Certifique-se de que os arquivos CSV estejam em:

```bash
data/
└── raw/
├── users.csv
├── accounts.csv
├── cards.csv
├── features.csv
└── news.csv

```
---

### 5. Executar o pipeline ETL

python -m src.main_etl


--

### 5. Executar o pipeline ETL

python -m src.main_etl

cpp
Copiar código

O arquivo final será salvo em:

data/processed/users_enriched.csv

yaml
Copiar código

---

## 🧠 Lógica do ETL (Resumo)

### Extract (extração)

O pipeline lê os seguintes arquivos:

- users.csv  
- accounts.csv  
- cards.csv  
- features.csv  
- news.csv  

---

### Transform (transformação)

Operações realizadas:

- Junção das tabelas  
- Contagem de features por usuário (`features_count`)  
- Contagem de notícias por usuário (`news_count`)  
- Cálculo de métricas derivadas:
  - `account_utilization = balance / limit`
  - `card_segment` (basic, gold, platinum, black, sem_cartao)
  - `engagement_score`

---

### Load (carregamento)

O arquivo final é exportado para:

data/processed/users_enriched.csv

yaml
Copiar código

---

## 📁 Estrutura do Projeto

```bash
.
├── data
│ ├── raw
│ │ ├── users.csv
│ │ ├── accounts.csv
│ │ ├── cards.csv
│ │ ├── features.csv
│ │ └── news.csv
│ └── processed
│ └── users_enriched.csv
├── src
│ ├── etl
│ │ ├── init.py
│ │ ├── extract.py
│ │ ├── transform.py
│ │ └── load.py
│ └── main_etl.py
├── requirements.txt
└── README.md
```

---

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- Pandas

---

## 📈 Possíveis Evoluções Futuras

- Testes unitários  
- Dockerfile  
- Integração com banco de dados  
- CI/CD  
- Dashboard (Power BI, Metabase etc.)

===========================================
