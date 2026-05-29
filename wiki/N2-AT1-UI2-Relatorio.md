## Relatório de Execução — Teste de Interface 2: Agendamento de Consulta

### Tela testada
Agendamento de Consulta — `http://localhost:3000` (menu Consultas)

### Ambiente de Testes

| Item | Valor |
|------|-------|
| Ferramenta | Robot Framework + SeleniumLibrary |
| Navegador | Google Chrome |
| Ambiente | Localhost |
| URL | http://localhost:3000 |
| Data de execução | 29/05/2026 |

### Comando de execução

```bash
python -m robot --outputdir tests/robot/results/agendamento tests/robot/agendamento_test.robot
```

### Evidências dos Casos de Teste

| Caso de Teste | Resultado Esperado | Resultado Obtido | Status |
|---------------|-------------------|-----------------|--------|
| CT01 — Data vazia | "Data obrigatória" | "Data obrigatória" | ✅ Aprovado |
| CT02 — Data passada | "Data inválida" | "Data inválida" | ✅ Aprovado |
| CT03 — Data futura válida | "Consulta agendada com sucesso" | "Consulta agendada com sucesso" | ✅ Aprovado |

### Arquivos de Evidência

| Arquivo | Descrição | Link |
|---------|-----------|------|
| report.html | Resumo executivo da execução | [report.html](https://github.com/isafmcl/VitalityWay/blob/main/tests/robot/results/agendamento/report.html) |
| log.html | Log detalhado da execução | [log.html](https://github.com/isafmcl/VitalityWay/blob/main/tests/robot/results/agendamento/log.html) |
| output.xml | Resultado bruto | [output.xml](https://github.com/isafmcl/VitalityWay/blob/main/tests/robot/results/agendamento/output.xml) |

> **Dica:** Abra o `report.html` no navegador e tire um print para anexar na wiki como evidência visual.

### Resumo

| Total de testes | Aprovados | Reprovados |
|-----------------|-----------|------------|
| 3 | 3 | 0 |

### Conclusão

Os três casos de teste automatizados confirmaram que a tela de agendamento valida corretamente o campo de data, aceitando datas válidas e rejeitando campos vazios ou datas passadas, conforme as partições de equivalência definidas na modelagem.
