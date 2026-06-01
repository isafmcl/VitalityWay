*** Settings ***
Library    SeleniumLibrary

Suite Setup       Abrir navegador na tela de login
Suite Teardown    Fechar navegador
Test Setup        Garantir tela de login

*** Variables ***
${URL}            http://localhost:5500
${BROWSER}        chrome
${INPUT_EMAIL}    id=login-email
${INPUT_SENHA}    id=login-senha
${BTN_ENTRAR}     css=#form-login button[type=submit]
${MSG}            id=msg-login
${TITULO_HOME}    id=home-boas-vindas

*** Test Cases ***

CT01 - Deve realizar login com credenciais válidas
    [Documentation]    Partição P3 — credenciais válidas → login realizado com sucesso
    Dado que o usuário informa o e-mail    cuidador@email.com
    E informa a senha    12345678
    Quando clicar em Entrar
    Então o sistema deve exibir a página inicial

CT02 - Deve exibir erro ao deixar e-mail vazio
    [Documentation]    Partição P1 — e-mail vazio → mensagem "E-mail obrigatório"
    Dado que o usuário informa o e-mail    ${EMPTY}
    E informa a senha    12345678
    Quando clicar em Entrar
    Então o sistema deve apresentar a mensagem    E-mail obrigatório

CT03 - Deve exibir erro ao deixar senha vazia
    [Documentation]    Partição P2 — senha vazia → mensagem "Senha obrigatória"
    Dado que o usuário informa o e-mail    cuidador@email.com
    E informa a senha    ${EMPTY}
    Quando clicar em Entrar
    Então o sistema deve apresentar a mensagem    Senha obrigatória

CT04 - Deve exibir erro com credenciais inválidas
    [Documentation]    Partição P4 — senha errada → mensagem "Credenciais inválidas"
    Dado que o usuário informa o e-mail    cuidador@email.com
    E informa a senha    senhaerrada
    Quando clicar em Entrar
    Então o sistema deve apresentar a mensagem    Credenciais inválidas

*** Keywords ***

Abrir navegador na tela de login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${INPUT_EMAIL}    timeout=10s

Garantir tela de login
    Go To    ${URL}
    Execute JavaScript    localStorage.clear()
    Reload Page
    Wait Until Element Is Visible    ${INPUT_EMAIL}    timeout=10s
    Sleep    0.5s

Dado que o usuário informa o e-mail
    [Arguments]    ${email}=${EMPTY}
    Wait Until Element Is Visible    ${INPUT_EMAIL}    timeout=5s
    Execute JavaScript    document.getElementById('login-email').value = '${email}';

E informa a senha
    [Arguments]    ${senha}=${EMPTY}
    Wait Until Element Is Visible    ${INPUT_SENHA}    timeout=5s
    Execute JavaScript    document.getElementById('login-senha').value = '${senha}';

Quando clicar em Entrar
    Submit Form    id=form-login
    Sleep    1s

Então o sistema deve exibir a página inicial
    Wait Until Element Is Visible    ${TITULO_HOME}    timeout=5s
    Element Should Contain    ${TITULO_HOME}    Olá

Então o sistema deve apresentar a mensagem
    [Arguments]    ${mensagem_esperada}
    Wait Until Element Is Visible    css=#msg-login.show    timeout=8s
    ${texto}=    Get Text    ${MSG}
    Should Be Equal As Strings    ${texto}    ${mensagem_esperada}

Fechar navegador
    Close Browser
