const hideMsgTimers = {};

function showPage(name) {
  document.querySelectorAll(".page").forEach((page) => page.classList.remove("active"));
  const targetPage = document.getElementById("page-" + name);
  if (targetPage) {
    targetPage.classList.add("active");
    window.scrollTo(0, 0);
  }
}

function showMsg(id, texto, tipo) {
  if (hideMsgTimers[id]) {
    clearTimeout(hideMsgTimers[id]);
    delete hideMsgTimers[id];
  }

  const el = document.getElementById(id);
  el.textContent = texto;
  el.className = "mensagem " + tipo + " show";

  if (tipo === "sucesso") {
    setTimeout(() => hideMsg(id), 5000);
  }
}

function hideMsg(id) {
  if (hideMsgTimers[id]) {
    clearTimeout(hideMsgTimers[id]);
  }

  const el = document.getElementById(id);
  el.classList.remove("show");
  hideMsgTimers[id] = setTimeout(() => {
    el.className = "mensagem";
    delete hideMsgTimers[id];
  }, 300);
}

function setNavigationVisible(visible) {
  const nav = document.getElementById("nav-links");
  nav.style.display = visible ? "flex" : "none";
}

function updateWelcomeText(nome) {
  document.getElementById("home-boas-vindas").textContent = `👋 Olá, ${nome}!`;
}

function resetForm(formId) {
  const form = document.getElementById(formId);
  if (form) {
    form.reset();
  }
}

function fillSelect(elementId, items, parser) {
  const select = document.getElementById(elementId);
  select.innerHTML = '<option value="">Selecione...</option>';
  items.forEach((item) => {
    const option = document.createElement("option");
    const parsed = parser(item);
    option.value = parsed.value;
    option.textContent = parsed.label;
    select.appendChild(option);
  });
}

function renderConsultationRows(consultas, medMap, idososMap) {
  const tbody = document.getElementById("tbody-consultas");
  if (consultas.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="4" style="text-align:center; color:#999; padding:20px;">
          📭 Nenhuma consulta agendada
        </td>
      </tr>
    `;
    return;
  }

  tbody.innerHTML = consultas
    .map((consulta) => {
      const statusLabel = consulta.status === "agendada" ? "📅 Agendada" : consulta.status;
      return `
        <tr>
          <td>${idososMap[consulta.idosoId] || consulta.idosoId}</td>
          <td>${medMap[consulta.medicoId] || consulta.medicoId}</td>
          <td>${consulta.data} ${consulta.hora}</td>
          <td><span class="badge ${consulta.status}">${statusLabel}</span></td>
        </tr>
      `;
    })
    .join("");
}
