# 09 - Tratar erros da API

## Objetivo

Evitar que o pipeline quebre silenciosamente em falhas de API.

## Entrega

Tratamento basico para status code, timeout e resposta invalida.

## Checklist

- Definir timeout na chamada HTTP.
- Tratar status code diferente de `200`.
- Exibir mensagem amigavel de erro.
- Garantir que erro nao gere arquivo raw invalido.

## Criterio de aceite

Uma chamada para recurso inexistente falha com mensagem clara e sem arquivo corrompido.

