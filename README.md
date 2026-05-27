# Des4AWSDIO
Repositorio para atividade (Gerado no Claude)

# Automação de Processos com AWS Lambda e Amazon S3

Anotações, insights e documentação prática do laboratório de automação serverless desenvolvido para a DIO (Digital Innovation One).

## 📌 Objetivo do Projeto
Este repositório serve como guia de estudos e portfólio, consolidando os conceitos de computação serverless (sem servidor) e armazenamento em nuvem na AWS. O foco principal é a integração do **AWS Lambda** para reagir automaticamente a eventos gerados no **Amazon S3**.

---

## 🏗️ Arquitetura do Projeto

O fluxo da automação segue o modelo baseado em eventos (*Event-Driven Architecture*):



1. **Upload de Arquivo:** O usuário ou um sistema faz o upload de um arquivo (imagem, CSV, JSON, etc.) para um bucket do Amazon S3.
2. **Notificação de Evento:** O S3 detecta o evento (ex: `s3:ObjectCreated:*`) e dispara uma notificação para o AWS Lambda.
3. **Execução Serverless:** A função Lambda é acordada, recebe os metadados do arquivo e executa a lógica programada (ex: redimensionamento de imagem, processamento de dados, carga em banco de dados).

---

## 🛠️ Tecnologias e Conceitos Chave

* **Amazon S3 (Simple Storage Service):** Serviço de armazenamento de objetos escalável, utilizado para guardar os arquivos de entrada e/ou saída.
* **AWS Lambda:** Serviço de computação que executa seu código em resposta a eventos e gerencia automaticamente os recursos de computação subjacentes.
* **IAM (Identity and Access Management):** Configuração de permissões cruciais (Políticas e Funções/Roles) para que o Lambda tenha direito de ler e escrever no bucket S3.
* **S3 Object Lambda:** Conceito avançado que permite adicionar código próprio a solicitações `GET` do S3 para modificar dados à medida que retornam para uma aplicação.

---

## 🚀 Insights Práticos e Aprendizados

Durante o desenvolvimento do laboratório, destaco as seguintes descobertas:

1. **Gestão de Permissões (Least Privilege):** No início, o Lambda pode falhar ao tentar acessar o S3. É fundamental garantir que a *Execution Role* do Lambda possua a política `AmazonS3ReadOnlyAccess` ou uma política personalizada mais restrita para segurança.
2. **Variáveis de Ambiente:** Configurar o nome dos buckets de destino como variáveis de ambiente no Lambda torna o código portátil e fácil de migrar entre ambientes de Desenvolvimento, Homologação e Produção.
3. **Idempotência:** Como os eventos do S3 podem, em cenários raros, ser disparados mais de uma vez, a função Lambda deve ser projetada para ser idempotente (ou seja, produzir o mesmo resultado mesmo se o mesmo arquivo for processado duas vezes).

---
