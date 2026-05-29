## Implementação Robot Framework — Teste de Interface 1: Login

### Arquivo de teste automatizado

O script Robot Framework que implementa os casos de teste CT01 a CT04 está disponível no repositório:

**Arquivo:** `tests/robot/login_test.robot`

**Link:** https://github.com/isafmcl/VitalityWay/blob/main/tests/robot/login_test.robot

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
python -m robot --outputdir tests/robot/results/login tests/robot/login_test.robot
```

### Casos implementados no arquivo

| Caso | Descrição no `.robot` |
|------|------------------------|
| CT01 | Deve realizar login com credenciais válidas |
| CT02 | Deve exibir erro ao deixar e-mail vazio |
| CT03 | Deve exibir erro ao deixar senha vazia |
| CT04 | Deve exibir erro com credenciais inválidas |

### Credenciais utilizadas nos testes

| Campo | Valor |
|-------|-------|
| E-mail | cuidador@email.com |
| Senha | 12345678 |
