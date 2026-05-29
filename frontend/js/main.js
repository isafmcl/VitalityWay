let token = null;
const idososMap = { i1: "Maria Aparecida", i2: "José Ferreira" };
const PAGINAS_PROTEGIDAS = ["home", "medicos", "consultas"];

async function iniciarAplicacao() {
  bindEvents();

  const savedToken = localStorage.getItem("vitalityway_token");
  const savedUserName = localStorage.getItem("vitalityway_user_name");

  if (savedToken && savedUserName) {
    const { ok, payload } = await validarSessaoApi(savedToken);

    if (ok && payload && payload.dados) {
      token = savedToken;
      const userName = payload.dados.usuario.nome || savedUserName;
      localStorage.setItem("vitalityway_user_name", userName);
      setNavigationVisible(true);
      updateWelcomeText(userName);
      navigateTo("home");
      return;
    }

    limparSessao(false);
  }

  setNavigationVisible(false);
  navigateTo("login");
}

function bindEvents() {
  document.getElementById("form-login").addEventListener("submit", fazerLogin);
  document.getElementById("form-medico").addEventListener("submit", cadastrarMedico);
  document.getElementById("form-consulta").addEventListener("submit", agendarConsulta);
  document.getElementById("form-signup").addEventListener("submit", fazerCadastro);
  document.getElementById("btn-home").addEventListener("click", () => navigateTo("home"));
  document.getElementById("btn-medicos").addEventListener("click", () => navigateTo("medicos"));
  document.getElementById("btn-consultas").addEventListener("click", () => navigateTo("consultas"));
  document.getElementById("btn-logout").addEventListener("click", logout);
  document.getElementById("link-signup").addEventListener("click", (e) => {
    e.preventDefault();
    navigateTo("signup");
  });
  document.getElementById("link-login-from-signup").addEventListener("click", (e) => {
    e.preventDefault();
    navigateTo("login");
  });
}

function dataMinimaConsulta() {
  return new Date().toISOString().split("T")[0];
}

function normalizarHora(valor) {
  return (valor || "").trim().slice(0, 5);
}

function validarDataConsulta(dataStr) {
  if (!dataStr) return "Data obrigatória";
  const hoje = dataMinimaConsulta();
  if (dataStr < hoje) return "Data inválida";
  return null;
}

function validarEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

function limparSessao(resetForms) {
  token = null;
  localStorage.removeItem("vitalityway_token");
  localStorage.removeItem("vitalityway_user_name");
  setNavigationVisible(false);

  if (resetForms) {
    document.getElementById("form-login").reset();
    document.getElementById("form-signup").reset();
  }
}

function exigirAutenticacao() {
  if (token) return true;
  setNavigationVisible(false);
  navigateTo("login");
  return false;
}

function tratarSessaoExpirada(response) {
  if (response && response.status === 401) {
    limparSessao(true);
    showMsg("msg-login", "Sessão expirada. Faça login novamente.", "erro");
    navigateTo("login");
    return true;
  }
  return false;
}

async function fazerLogin(event) {
  event.preventDefault();
  hideMsg("msg-login");

  const email = document.getElementById("login-email").value.trim();
  const senha = document.getElementById("login-senha").value;

  if (!email) {
    showMsg("msg-login", "E-mail obrigatório", "erro");
    return;
  }

  if (!validarEmail(email)) {
    showMsg("msg-login", "E-mail inválido", "erro");
    return;
  }

  if (!senha) {
    showMsg("msg-login", "Senha obrigatória", "erro");
    return;
  }

  const { ok, payload } = await loginApi(email, senha);

  if (ok && payload && payload.dados) {
    token = payload.dados.token;
    const userName = payload.dados.usuario.nome;

    localStorage.setItem("vitalityway_token", token);
    localStorage.setItem("vitalityway_user_name", userName);

    setNavigationVisible(true);
    updateWelcomeText(userName);
    navigateTo("home");
  } else {
    const msg = payload ? payload.mensagem || "Erro ao fazer login" : "Resposta inválida do servidor";
    showMsg("msg-login", msg, "erro");
  }
}

async function fazerCadastro(event) {
  event.preventDefault();
  hideMsg("msg-signup");

  const nome = document.getElementById("signup-nome").value.trim();
  const email = document.getElementById("signup-email").value.trim();
  const senha = document.getElementById("signup-senha").value;
  const btn = event.target.querySelector('button[type="submit"]');

  if (!nome || nome.length < 3) {
    showMsg("msg-signup", "Nome deve ter pelo menos 3 caracteres", "erro");
    return;
  }

  if (!validarEmail(email)) {
    showMsg("msg-signup", "E-mail inválido", "erro");
    return;
  }

  if (senha.length < 6) {
    showMsg("msg-signup", "Senha deve ter pelo menos 6 caracteres", "erro");
    return;
  }

  if (btn) {
    btn.disabled = true;
    btn.textContent = "Cadastrando...";
  }

  const { ok, payload } = await signupApi(email, senha, nome);

  if (btn) {
    btn.disabled = false;
    btn.textContent = "Cadastrar";
  }

  if (ok) {
    document.getElementById("form-signup").reset();
    limparSessao(false);
    navigateTo("login");
    document.getElementById("login-email").value = email;
    showMsg("msg-login", "Cadastro realizado! Faça login para continuar.", "sucesso");
  } else {
    const msg = payload ? payload.mensagem || "Erro ao cadastrar" : "Resposta inválida do servidor";
    showMsg("msg-signup", msg, "erro");
  }
}

function logout() {
  limparSessao(true);
  navigateTo("login");
}

async function navigateTo(page) {
  if (PAGINAS_PROTEGIDAS.includes(page) && !exigirAutenticacao()) {
    return;
  }

  showPage(page);

  if (page === "medicos") {
    await carregarEspecialidades();
  }
  if (page === "consultas") {
    await carregarDadosConsulta();
  }
}

async function carregarEspecialidades() {
  const { ok, payload, status } = await listarEspecialidadesApi();
  if (tratarSessaoExpirada({ status })) return;
  if (!ok) {
    showMsg("msg-medico", (payload && payload.mensagem) || "Erro ao carregar especialidades", "erro");
    return;
  }
  fillSelect("med-esp", payload.dados, (item) => ({ value: item.id, label: item.nome }));
}

async function cadastrarMedico(event) {
  event.preventDefault();
  hideMsg("msg-medico");

  if (!exigirAutenticacao()) return;

  const nome = document.getElementById("med-nome").value.trim();
  const crm = document.getElementById("med-crm").value.trim();
  const especialidadeId = document.getElementById("med-esp").value;

  if (!nome || nome.length < 3) {
    showMsg("msg-medico", "Nome deve ter pelo menos 3 caracteres", "erro");
    return;
  }

  if (!crm || crm.length < 5) {
    showMsg("msg-medico", "CRM inválido", "erro");
    return;
  }

  if (!especialidadeId) {
    showMsg("msg-medico", "Selecione uma especialidade", "erro");
    return;
  }

  const { ok, payload, status } = await cadastrarMedicoApi(token, { nome, crm, especialidadeId });
  if (tratarSessaoExpirada({ status })) return;

  if (ok) {
    showMsg("msg-medico", payload.mensagem, "sucesso");
    resetForm("form-medico");
  } else {
    showMsg("msg-medico", (payload && payload.mensagem) || "Erro ao cadastrar", "erro");
  }
}

async function carregarDadosConsulta() {
  document.getElementById("con-data").min = dataMinimaConsulta();

  const medicosResponse = await listarMedicosApi();
  if (tratarSessaoExpirada(medicosResponse)) return;

  if (!medicosResponse.ok) {
    showMsg("msg-consulta", (medicosResponse.payload && medicosResponse.payload.mensagem) || "Erro ao listar médicos", "erro");
    return;
  }

  const medicos = medicosResponse.payload.dados;
  fillSelect("con-medico", medicos, (item) => ({ value: item.id, label: item.nome }));
  await carregarConsultas();
}

async function agendarConsulta(event) {
  event.preventDefault();
  hideMsg("msg-consulta");

  if (!exigirAutenticacao()) return;

  const idosoId = document.getElementById("con-idoso").value;
  const medicoId = document.getElementById("con-medico").value;
  const data = document.getElementById("con-data").value;
  const hora = normalizarHora(document.getElementById("con-hora").value);
  const local = document.getElementById("con-local").value.trim();

  if (!idosoId) {
    showMsg("msg-consulta", "Selecione um idoso", "erro");
    return;
  }

  if (!medicoId) {
    showMsg("msg-consulta", "Selecione um médico", "erro");
    return;
  }

  const erroData = validarDataConsulta(data);
  if (erroData) {
    showMsg("msg-consulta", erroData, "erro");
    return;
  }

  if (!hora) {
    showMsg("msg-consulta", "Selecione uma hora", "erro");
    return;
  }

  if (!local || local.length < 3) {
    showMsg("msg-consulta", "Local deve ter pelo menos 3 caracteres", "erro");
    return;
  }

  const response = await agendarConsultaApi(token, { idosoId, medicoId, data, hora, local });
  if (tratarSessaoExpirada(response)) return;

  if (response.ok) {
    showMsg("msg-consulta", response.payload.mensagem, "sucesso");
    resetForm("form-consulta");
    document.getElementById("con-data").min = dataMinimaConsulta();
    await carregarConsultas();
  } else {
    showMsg("msg-consulta", (response.payload && response.payload.mensagem) || "Erro ao agendar", "erro");
  }
}

async function carregarConsultas() {
  const { ok, payload, status } = await listarConsultasApi();
  if (tratarSessaoExpirada({ status })) return;

  if (!ok) {
    showMsg("msg-consulta", (payload && payload.mensagem) || "Erro ao listar consultas", "erro");
    return;
  }

  const medicosResponse = await listarMedicosApi();
  const medMap = {};
  if (medicosResponse.ok && medicosResponse.payload) {
    medicosResponse.payload.dados.forEach((m) => (medMap[m.id] = m.nome));
  }

  renderConsultationRows(payload.dados, medMap, idososMap);
}

window.navigateTo = navigateTo;
window.addEventListener("DOMContentLoaded", iniciarAplicacao);
