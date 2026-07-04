# DataForge

Projeto de estudos em Engenharia de Dados, começando pela Sprint 1: ambiente, Git e base em Python.

## Objetivo da Sprint 1

Criar uma estrutura inicial de projeto e um script Python simples que:

- pede nome e idade;
- estima a quantidade de dias vividos;
- salva o resultado em `data/raw/user_profile.json`.

## Estrutura

```text
dataforge/
  src/
    main.py
  data/
    raw/
    processed/
  docs/
  requirements.txt
```

## Como rodar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python src\main.py
```