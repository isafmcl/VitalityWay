## Modelagem — Teste de Interface 1: Login

**Tela testada:** Tela de Login (`http://localhost:3000`)

**Técnica: Particionamento de Equivalência**

### Interface

A tela de login possui dois campos obrigatórios (e-mail e senha) e um botão "Entrar". O sistema valida os campos antes de enviar a requisição à API.

### Partições de Equivalência

**Campo: E-mail**

| Índice | Partição | Descrição | Resultado Esperado |
|--------|----------|-----------|-------------------|
| P1 | E-mail vazio | Campo não preenchido | Mensagem "E-mail obrigatório" |
| P2 | E-mail inválido | Valor sem formato de e-mail | Mensagem "E-mail inválido" |
| P3 | E-mail válido | Formato correto e existente no sistema | Continua validação |

**Campo: Senha**

| Índice | Partição | Descrição | Resultado Esperado |
|--------|----------|-----------|-------------------|
| P1 | Senha vazia | Campo não preenchido | Mensagem "Senha obrigatória" |
| P2 | Senha errada | Valor diferente do cadastrado | Mensagem "Credenciais inválidas" |
| P3 | Senha correta | Valor igual ao cadastrado | Login realizado, redireciona para início |

### Casos de Teste Derivados

| Caso | E-mail | Senha | Resultado Esperado |
|------|--------|-------|--------------------|
| CT01 | cuidador@email.com | 12345678 | Página inicial exibida |
| CT02 | (vazio) | 12345678 | "E-mail obrigatório" |
| CT03 | cuidador@email.com | (vazio) | "Senha obrigatória" |
| CT04 | cuidador@email.com | senhaerrada | "Credenciais inválidas" |
