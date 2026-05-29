# Como publicar os testes de Interface na Wiki

## Páginas que você precisa criar (Perguntas 9 a 14)

| Pergunta | Nome da página na Wiki | Arquivo pronto |
|----------|------------------------|----------------|
| 9 | N2-AT1-UI1-Modelagem | `wiki/N2-AT1-UI1-Modelagem.md` |
| 10 | N2-AT1-UI1-Robot | `wiki/N2-AT1-UI1-Robot.md` |
| 11 | N2-AT1-UI1-Relatorio | `wiki/N2-AT1-UI1-Relatorio.md` |
| 12 | N2-AT1-UI2-Modelagem | `wiki/N2-AT1-UI2-Modelagem.md` |
| 13 | N2-AT1-UI2-Robot | `wiki/N2-AT1-UI2-Robot.md` |
| 14 | N2-AT1-UI2-Relatorio | `wiki/N2-AT1-UI2-Relatorio.md` |

## Passo a passo

### 1. Subir backend e frontend

```powershell
# Terminal 1
cd backend
python app.py

# Terminal 2
cd frontend
python -m http.server 3000
```

### 2. Rodar os testes Robot

```powershell
pip install robotframework robotframework-seleniumlibrary

cd vitalityway
python -m robot --outputdir tests/robot/results/login tests/robot/login_test.robot
python -m robot --outputdir tests/robot/results/agendamento tests/robot/agendamento_test.robot
```

Resultado esperado: **4 testes passando** (login) + **3 testes passando** (agendamento).

### 3. Subir tudo no GitHub

Inclua no repositório:
- `tests/robot/login_test.robot`
- `tests/robot/agendamento_test.robot`
- `tests/robot/results/login/report.html` (evidência)
- `tests/robot/results/agendamento/report.html` (evidência)
- pasta `wiki/` com os arquivos `.md`

### 4. Criar páginas na Wiki do GitHub

1. Abra seu repositório no GitHub
2. Clique na aba **Wiki**
3. Para cada página, clique em **New Page**
4. Use o **nome exato** da tabela acima como título
5. Copie e cole o conteúdo do arquivo `.md` correspondente
6. Os links já apontam para `https://github.com/isafmcl/VitalityWay`
7. Salve a página

### 5. Anexar prints (recomendado)

Abra no navegador:
- `tests/robot/results/login/report.html`
- `tests/robot/results/agendamento/report.html`

Tire print da tela verde com todos os testes passando e cole nas páginas de **Relatório**.

### 6. Enviar ao professor

Envie:
- Link da Wiki
- Link do repositório GitHub
