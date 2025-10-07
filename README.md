# 🛠️ Projeto ETL Geoespacial com Docker, MinIO, PostgreSQL e Spark

Este projeto implementa uma **pipeline ETL (Extract, Transform, Load)** com foco em dados geoespaciais públicos do U.S. Census Bureau, utilizando tecnologias modernas de processamento e armazenamento de dados em um ambiente **100% Dockerizado**.

## 📦 Tecnologias Utilizadas

- **Docker Compose** – Orquestração de ambientes
- **MinIO** – Data Lake S3-compatible para armazenamento bruto
- **PostgreSQL** – Banco de dados relacional para os dados tratados
- **Apache Spark** – Motor de processamento para transformação de dados
- **Python + GeoPandas** – Scripts de extração e manipulação geográfica

---

## ⚙️ Requisitos

Para executar este projeto localmente, é necessário ter:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🧪 Componentes do Ambiente

Este projeto depende dos seguintes containers, definidos via `docker-compose.yml`:

| Serviço     | Função                             |
|-------------|------------------------------------|
| **MinIO**   | Armazena os dados brutos (.shp etc) como data lake |
| **PostgreSQL** | Banco de dados destino para os dados transformados |
| **Spark**   | Responsável por processar os dados extraídos e carregá-los |
| **ETL (Python)** | Scripts responsáveis por baixar, extrair, transformar e carregar os dados |

---

## 🚀 Executando o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/alcidescoutinho95-bit/etl-kaggle-geoloc.git
   cd etl-kaggle-geoloc
