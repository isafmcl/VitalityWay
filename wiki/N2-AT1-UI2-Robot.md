## Implementação Robot Framework — Teste de Interface 2: Agendamento

### Arquivo de teste automatizado

O script Robot Framework que implementa os casos de teste CT01 a CT03 está disponível no repositório:

**Arquivo:** `tests/robot/agendamento_test.robot`

**Link:** https://github.com/isafmcl/VitalityWay/blob/main/tests/robot/agendamento_test.robot

### Pré-requisitos

- Backend rodando em `http://localhost:5000`
- Frontend rodando em `http://localhost:3000`
- Python com Robot Framework instalado:
  ```bash
  pip install robotframework robotframework-seleniumlibrary
  ```
- Google Chrome instalado

### Comando de execução

```bash
cd vitalityway
python -m robot --outputdir tests/robot/results/agendamento tests/robot/agendamento_test.robot
```

### Casos implementados no arquivo

| Caso | Descrição no `.robot` |
|------|------------------------|
| CT01 | Deve exibir erro quando data não é preenchida |
| CT02 | Deve exibir erro quando data é passada |
| CT03 | Deve agendar consulta com data futura válida |

### Fluxo do teste

1. Abre o navegador em `http://localhost:3000`
2. Faz login com `cuidador@email.com` / `12345678`
3. Navega para a tela de Consultas
4. Executa cada caso de teste isolando validações do campo **data**
