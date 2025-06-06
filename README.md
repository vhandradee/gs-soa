# GS-SOA — Sistema de Resposta a Quedas de Energia

Este projeto foi desenvolvido como parte da entrega da disciplina de Arquitetura Orientada a Serviço, integrando uma solução em Python com FastAPI e uma API complementar em Java com Spring Boot.

## Integrantes do Grupo

- **Felipe Capriotti** – RM98460  
- **Manoella Herrerias Waideman** – RM98906  
- **Victor Hugo Andrade** – RM550996
 
## Objetivo

O **GS-SOA** (anteriormente chamado Guard Blackout) tem como objetivo identificar e responder rapidamente a quedas de energia em bairros afetados, simulando uma arquitetura real de serviços independentes.

## Requisitos da Arquitetura Orientada a Serviço

Consumo de APIs RESTful  
Organização modular (camadas separadas)  
Separação de controle, serviço e dados  
Uso de padrões REST e JSON

## Backend Principal — Python (FastAPI)

### Estrutura

- `main.py` — ponto de entrada da API
- `services/` — lógica de simulação de quedas
- `models/` — banco de dados SQLite
- `requirements.txt` — dependências do projeto

### Como rodar

```bash
uvicorn main:app --reload
