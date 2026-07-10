# 23 - Criar reprocessamento simples

## Objetivo

Permitir rodar novamente uma etapa usando dados ja salvos.

## Entrega

Modo simples de reprocessar arquivos raw.

## Checklist

- Ler JSON existente em `data/raw/`.
- Transformar novamente para trusted.
- Evitar chamada de API quando nao for necessaria.
- Documentar quando usar reprocessamento.

## Criterio de aceite

E possivel recriar a camada trusted a partir dos dados raw.

