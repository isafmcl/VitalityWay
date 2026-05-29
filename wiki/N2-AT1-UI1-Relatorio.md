## Relatório de Execução — Teste de Interface 1: Login

### Tela testada
Login — `http://localhost:3000`

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
python -m robot --outputdir tests/robot/results/login tests/robot/login_test.robot
```

### Evidências dos Casos de Teste

| Caso de Teste | Resultado Esperado | Resultado Obtido | Status |
|---------------|-------------------|-----------------|--------|
| CT01 — Login válido | Página inicial exibida | Página inicial exibida | ✅ Aprovado |
| CT02 — E-mail vazio | "E-mail obrigatório" | "E-mail obrigatório" | ✅ Aprovado |
| CT03 — Senha vazia | "Senha obrigatória" | "Senha obrigatória" | ✅ Aprovado |
| CT04 — Credenciais inválidas | "Credenciais inválidas" | "Credenciais inválidas" | ✅ Aprovado |

### Arquivos de Evidência

| Arquivo | Descrição | Link |
|---------|-----------|------|
| report.html | Resumo executivo da execução | [report.html](https://github.com/isafmcl/VitalityWay/blob/main/tests/robot/results/login/report.html) |
| log.html | Log detalhado da execução | [log.html](https://github.com/isafmcl/VitalityWay/blob/main/tests/robot/results/login/log.html) |
| output.xml | Resultado bruto | [output.xml](https://github.com/isafmcl/VitalityWay/blob/main/tests/robot/results/login/output.xml) |

> **Dica:** Abra o `report.html` no navegador e tire um print para anexar na wiki como evidência visual.

### Resumo

| Total de testes | Aprovados | Reprovados |
|-----------------|-----------|------------|
| 4 | 4 | 0 |

### Conclusão

Os quatro casos de teste automatizados com Robot Framework apresentaram conformidade com o comportamento esperado da tela de login, validando corretamente as partições de equivalência definidas na modelagem.
