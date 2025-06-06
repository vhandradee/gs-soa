# GS-SOA — Sistema de Resposta a Quedas de Energia

Este projeto foi desenvolvido como parte da entrega da disciplina de Arquitetura Orientada a Serviço, integrando uma solução em Python com FastAPI e uma API complementar em Java com Spring Boot.

---

## Integrantes do Grupo

- Felipe Capriotti – RM98460  
- Manoella Herrerias Waideman – RM98906  
- Victor Hugo Andrade – RM550996

---

## Objetivo

O GS-SOA tem como objetivo identificar e responder rapidamente a quedas de energia em bairros afetados, simulando uma arquitetura real de serviços independentes.

---

## Entregas exigidas (Checklist da Avaliação)

| Critério                                                                
|-------------------------------------------------------------------------|-----------|
| 1. Implementar um código para consumir uma ou mais APIs RESTful ou SOAP   | Sim (em Python, simulação de consumo REST) |
| 2. Organização modular com serviços independentes e reutilizáveis         | Sim (camadas separadas por função) |
| 3. Separação clara entre camadas de controle, serviço e dados             | Sim (estruturado em pastas e pacotes em ambos os projetos) |
| 4. Uso de padrões como REST, JSON, XML, SOAP, WSDL                        | Sim (REST e JSON utilizados nos dois projetos) |
| 5. API desenvolvida em Java com banco de dados e endpoints                | Sim (Java Spring Boot com banco H2 e endpoints funcionando) |

---

## Backend Principal — Python (FastAPI)

### Estrutura

- `main.py` — ponto de entrada da API
- `services/` — lógica de simulação de quedas
- `models/` — banco de dados SQLite
- `requirements.txt` — dependências do projeto

### Como rodar

```bash
uvicorn main:app --reload


- Acesse: http://localhost:8000/docs

---

## API Complementar — Java (Spring Boot)

### Estrutura

- `controller/` — exposição dos endpoints
- `model/` — entidade Bairro
- `repository/` — acesso via Spring Data JPA
- Banco de dados: H2 (em memória)

### Como rodar

```bash
cd gssoa-java
mvn spring-boot:run
```

- Teste os endpoints:
  - GET http://localhost:8080/bairros
  - POST http://localhost:8080/bairros
- Acesse o banco: http://localhost:8080/h2-console
  - JDBC URL: jdbc:h2:mem:gssoa | User: sa

---

## Banco de Dados

### Python (FastAPI):
- Banco utilizado: SQLite
- Banco criado automaticamente como gssoa.db
- Tabela: quedas (id, bairro, tempo_estimado)

### Java (Spring Boot):
- Banco utilizado: H2 em memória
- Tabela: BAIRRO (id, nome, tempoEstimado)
- Acesso via H2 console no navegador
