# 🌿 VitalityWay

Sistema moderno e intuitivo para gerenciamento de consultas médicas para idosos. Com interface responsiva, design moderno e fluxo user-friendly.

## Melhorias Implementadas

✅ **Design Moderno** — Interface com gradiente, animações suaves e tipografia moderna (Google Fonts)  
✅ **Responsive** — Funciona perfeitamente em desktop e mobile  
✅ **UX Intuitiva** — Fluxo claro: Login → Cadastro → Home → Médicos/Consultas  
✅ **Feedback Visual** — Mensagens de sucesso/erro com animações  
✅ **Dark/Light Friendly** — Cores contrastantes e legibilidade garantida  
✅ **Ícones Visuais** — Emojis estrategicamente posicionados para facilitar compreensão  

## Estrutura do Projeto

```
vitalityway/
├── backend/
│   ├── app.py              ← ponto de entrada Flask
│   ├── requirements.txt
│   ├── core/               ← dados, erros, autenticação e utilitários
│   │   ├── auth.py
│   │   ├── data.py
│   │   ├── errors.py
│   │   └── utils.py
│   ├── routes/             ← rotas agrupadas em blueprints
│   │   ├── auth.py         (login, signup)
│   │   ├── medico.py
│   │   ├── consulta.py
│   │   └── catalog.py
│   └── services/           ← regras de negócio
│       ├── auth.py
│       ├── medico.py
│       ├── consulta.py
│       └── catalog.py
├── frontend/
│   ├── index.html         ← Interface web moderna
│   ├── css/
│   │   └── style.css      (design moderno, animações)
│   └── js/
│       ├── api.js         (chamadas ao backend)
│       ├── main.js        (lógica da aplicação)
│       └── ui.js          (manipulação do DOM)
└── tests/
    ├── api/
    │   └── VitalityWay_API_Tests.postman_collection.json
    └── robot/
        ├── login_test.robot
        └── agendamento_test.robot
```

## Como Rodar o Projeto

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

**Servidor sobe em:** `http://localhost:5000`

> Se a porta estiver ocupada:
> ```bash
> $env:PORT=5000; python app.py
> ```

### 2. Frontend

```bash
cd frontend
python -m http.server 3000
```

**Acesse:** `http://localhost:3000`

### Credenciais de Teste

| Email | Senha | Perfil |
|-------|-------|--------|
| `admin@email.com` | `admin123` | Admin |
| `cuidador@email.com` | `12345678` | Cuidador |

**Ou crie uma nova conta** clicando em "Cadastre-se aqui" na página de login.

## Design & UX

### Cores
- **Gradiente Principal**: `#667eea` → `#764ba2` (roxo moderno)
- **Fundo**: Gradiente vibrante em toda a aplicação
- **Cards**: Branco com sombras elegantes

### Tipografia
- **Font**: Inter (Google Fonts) — limpa e moderna
- **Headings**: Bold, com gradiente
- **Body**: Peso 400-500, legível

### Animações
-  Fade-in ao carregar páginas
-  Hover effects nos botões e cards
- Transições suaves nos inputs
-  Float animation nos ícones

##  Fluxo da Aplicação

```
┌─────────────────────────────────────┐
│  Login / Cadastro                    │
│  ✓ Login existente                  │
│  ✓ Criar nova conta (signup)        │
└──────────┬──────────────────────────┘
           │
           ↓
┌─────────────────────────────────────┐
│  Home (Dashboard)                    │
│  ✓ Boas-vindas personalizada       │
│  ✓ Acesso rápido a Médicos/Consultas│
└──────────┬───────────┬──────────────┘
           │           │
    ┌──────┘           └─────┐
    │                        │
    ↓                        ↓
┌──────────────────┐  ┌──────────────────┐
│ Médicos          │  │ Consultas        │
│ ✓ Cadastrar      │  │ ✓ Agendar        │
│ ✓ Listar todos   │  │ ✓ Listar         │
└──────────────────┘  │ ✓ Visualizar     │
                      └──────────────────┘
```

## API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/login` | Autenticação |
| POST | `/signup` | Cadastro de novo usuário |
| GET | `/especialidades` | Lista especialidades |
| GET | `/idosos` | Lista idosos |
| POST | `/medicos` | Cadastrar médico |
| GET | `/medicos` | Listar médicos |
| POST | `/consultas` | Agendar consulta |
| GET | `/consultas` | Listar consultas |
| GET | `/health` | Status do servidor |

## Testes

### Postman
```bash
# Importe a collection:
tests/api/VitalityWay_API_Tests.postman_collection.json
```

### Robot Framework
```bash
robot tests/robot/login_test.robot
robot tests/robot/agendamento_test.robot
```

## Stack Tecnológico

**Backend**
- Flask 3.0.3
- Flask-CORS 4.0.1
- Python 3.10+

**Frontend**
- HTML5
- CSS3 (com animações e gradientes)
- Vanilla JavaScript (sem dependências)
- Google Fonts (Inter)

## Princípios Aplicados

✅ **Clean Code** — Funções pequenas, nomes descritivos  
✅ **SOLID** — Single Responsibility, separação de concerns  
✅ **DRY** — Sem repetição de código  
✅ **Responsive Design** — Mobile-first, funciona em todos os tamanhos  
✅ **Acessibilidade** — Bom contraste, labels em inputs, ícones visuais  


### Executando os testes
```bash
cd tests/robot

# Teste de Login
robot login_test.robot

# Teste de Agendamento
robot agendamento_test.robot
```

Os relatórios são gerados automaticamente:
- `report.html` — resumo executivo
- `log.html` — log detalhado
- `output.xml` — resultado bruto

---

## Endpoints da API

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| GET | /health | Status da API | Não |
| POST | /login | Autenticação | Não |
| GET | /especialidades | Lista especialidades | Não |
| GET | /idosos | Lista idosos | Não |
| GET | /medicos | Lista médicos | Não |
| POST | /medicos | Cadastra médico | Sim |
| GET | /consultas | Lista consultas | Não |
| POST | /consultas | Agenda consulta | Sim |
