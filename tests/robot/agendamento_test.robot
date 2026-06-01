*** Settings ***
Library    SeleniumLibrary

Suite Setup       Fazer login e acessar tela de consultas
Suite Teardown    Fechar navegador
Test Setup        Garantir tela de consultas

*** Variables ***
${URL}              http://localhost:5500
${BROWSER}          chrome
${INPUT_EMAIL}      id=login-email
${INPUT_SENHA}      id=login-senha
${BTN_LOGIN}        css=#form-login button[type=submit]
${SEL_IDOSO}        id=con-idoso
${SEL_MEDICO}       id=con-medico
${INPUT_DATA}       id=con-data
${INPUT_HORA}       id=con-hora
${INPUT_LOCAL}      id=con-local
${BTN_AGENDAR}      css=#form-consulta button[type=submit]
${MSG}              id=msg-consulta

*** Test Cases ***

CT01 - Deve exibir erro quando data não é preenchida
    [Documentation]    Partição P1 — data vazia → "Data obrigatória"
    Dado que o usuário seleciona o idoso    i1
    E seleciona o médico    m1
    E informa a data    ${EMPTY}
    E informa a hora    10:00
    E informa o local    UBS Centro
    Quando clicar em Agendar
    Então o sistema deve apresentar a mensagem    Data obrigatória

CT02 - Deve exibir erro quando data é passada
    [Documentation]    Partição P2 — data no passado → "Data inválida"
    Dado que o usuário seleciona o idoso    i1
    E seleciona o médico    m1
    E informa a data    2020-01-01
    E informa a hora    10:00
    E informa o local    UBS Centro
    Quando clicar em Agendar
    Então o sistema deve apresentar a mensagem    Data inválida

CT03 - Deve agendar consulta com data futura válida
    [Documentation]    Partição P4 — data futura → "Consulta agendada com sucesso"
    Dado que o usuário seleciona o idoso    i1
    E seleciona o médico    m1
    E informa a data    2026-07-10
    E informa a hora    14:30
    E informa o local    UBS Centro
    Quando clicar em Agendar
    Então o sistema deve apresentar a mensagem    Consulta agendada com sucesso

*** Keywords ***

Fazer login e acessar tela de consultas
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${INPUT_EMAIL}    timeout=10s
    Input Text      ${INPUT_EMAIL}    cuidador@email.com
    Input Password  ${INPUT_SENHA}    12345678
    Click Button    ${BTN_LOGIN}
    Sleep    1s
    Execute JavaScript    navigateTo('consultas')
    Sleep    2s
    Wait Until Element Is Visible    ${SEL_IDOSO}    timeout=10s

Garantir tela de consultas
    Execute JavaScript    navigateTo('consultas')
    Sleep    1s
    Wait Until Element Is Visible    ${SEL_IDOSO}    timeout=10s

Dado que o usuário seleciona o idoso
    [Arguments]    ${idoso_id}
    Select From List By Value    ${SEL_IDOSO}    ${idoso_id}

E seleciona o médico
    [Arguments]    ${medico_id}
    Select From List By Value    ${SEL_MEDICO}    ${medico_id}

E informa a data
    [Arguments]    ${data}=${EMPTY}
    Execute JavaScript    document.getElementById('con-data').value = '${data}';

E informa a hora
    [Arguments]    ${hora}=${EMPTY}
    Execute JavaScript    document.getElementById('con-hora').value = '${hora}';

E informa o local
    [Arguments]    ${local}=${EMPTY}
    Clear Element Text    ${INPUT_LOCAL}
    Run Keyword If    '${local}' != '${EMPTY}'    Input Text    ${INPUT_LOCAL}    ${local}

Quando clicar em Agendar
    Click Button    ${BTN_AGENDAR}
    Sleep    1s

Então o sistema deve apresentar a mensagem
    [Arguments]    ${mensagem_esperada}
    Wait Until Element Is Visible    css=#msg-consulta.show    timeout=8s
    ${texto}=    Get Text    ${MSG}
    Should Be Equal As Strings    ${texto}    ${mensagem_esperada}

Fechar navegador
    Close Browser
