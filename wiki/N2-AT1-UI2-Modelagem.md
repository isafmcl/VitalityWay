## Modelagem — Teste de Interface 2: Agendamento de Consulta

**Tela testada:** Tela de Agendamento (`http://localhost:3000` → menu Consultas)

**Técnica: Particionamento de Equivalência com Análise de Valor Limite (BVA)**

### Interface

A tela de agendamento possui campos: Idoso (select), Médico (select), Data (input date), Hora (input time) e Local (input text). O campo Data é o foco desta modelagem.

### Partições de Equivalência — campo `data`

| Índice | Partição | Descrição | Resultado Esperado |
|--------|----------|-----------|-------------------|
| P1 | Data vazia | Campo não preenchido | "Data obrigatória" |
| P2 | Data passada | Data anterior ao dia atual | "Data inválida" |
| P3 | Data atual (BVA — fronteira inferior) | Data igual ao dia de hoje | Aceita agendamento |
| P4 | Data futura válida (BVA — acima da fronteira) | Data posterior ao dia atual | "Consulta agendada com sucesso" |

### Casos de Teste Derivados

| Caso | Data | Resultado Esperado |
|------|------|--------------------|
| CT01 | (vazio) | "Data obrigatória" |
| CT02 | 2020-01-01 | "Data inválida" |
| CT03 | 2026-07-10 | "Consulta agendada com sucesso" |

> Para CT01 e CT02, os demais campos (idoso, médico, hora, local) são preenchidos corretamente para isolar o campo data como único fator de falha.
