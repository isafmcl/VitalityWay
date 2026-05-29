const API_HOST = window.location.hostname || "localhost";
const API_PORT = 5000;
const API_BASE = `${window.location.protocol}//${API_HOST}:${API_PORT}`;

async function apiFetch(endpoint, options = {}) {
  try {
    const response = await fetch(API_BASE + endpoint, options);
    const payload = await response.json();
    return { ok: response.ok, status: response.status, payload };
  } catch (err) {
    return {
      ok: false,
      status: 0,
      payload: { mensagem: "Não foi possível conectar ao servidor. Verifique se o backend está rodando na porta " + API_PORT },
    };
  }
}

async function loginApi(email, senha) {
  const body = new URLSearchParams({ email, senha });
  return apiFetch("/login", { method: "POST", body });
}

async function signupApi(email, senha, nome) {
  const body = new URLSearchParams({ email, senha, nome });
  return apiFetch("/signup", { method: "POST", body });
}

async function validarSessaoApi(token) {
  const qs = token ? `?token=${encodeURIComponent(token)}` : "";
  return apiFetch("/session" + qs);
}

async function cadastrarMedicoApi(token, medico) {
  const qs = token ? `?token=${encodeURIComponent(token)}` : "";
  const body = new URLSearchParams(medico);
  return apiFetch("/medicos" + qs, { method: "POST", body });
}

async function listarMedicosApi() {
  return apiFetch("/medicos");
}

async function listarEspecialidadesApi() {
  return apiFetch("/especialidades");
}

async function agendarConsultaApi(token, consulta) {
  const qs = token ? `?token=${encodeURIComponent(token)}` : "";
  const body = new URLSearchParams(consulta);
  return apiFetch("/consultas" + qs, { method: "POST", body });
}

async function listarConsultasApi() {
  return apiFetch("/consultas");
}
