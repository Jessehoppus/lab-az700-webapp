# Lab AZ-700 - Web App Python (Flask)

Este repositório contém um exemplo de aplicação Python/Flask para o laboratório de **Application Gateway e Balanceamento de Carga (AZ-700)**.

## Deploy Automático
O GitHub Actions faz o deploy para o Azure Web App sempre que houver push na branch **main**.

## Endpoints
- `/` - Página de boas-vindas com informações da instância
- `/healthz` - Health check para o Application Gateway
- `/whoami` - Responde em JSON com dados da instância
