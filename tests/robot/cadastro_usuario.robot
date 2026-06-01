*** Settings ***
Library    SeleniumLibrary

Suite Setup       Abrir navegador na tela de cadastro
Suite Teardown    Fechar navegador
Test Setup        Garantir tela de cadastro

*** Variables ***
${URL}             http://localhost:3000
${BROWSER}         chrome
${LINK_CADASTRO}   id=link-signup
${INPUT_NOME}      id=signup-nome
${INPUT_EMAIL}     id=signup-email
${INPUT_SENHA}     id=signup-senha
${BTN_CADASTRAR}   css=#form-signup button[type=submit]
${MSG_LOGIN}       id=msg-login
${MSG_SIGNUP}      id=msg-signup

*** Test Cases ***

CT01 - Deve cadastrar usuário com dados válidos
    Dado que o usuário informa o nome    Guilherme Teste Robot
    E informa o email    guilherme.robot999@email.com
    E informa a senha    123456
    Quando clicar em Cadastrar
    Então o sistema deve exibir mensagem de cadastro realizado

CT02 - Deve exibir erro com nome inválido
    Dado que o usuário informa o nome    Gu
    E informa o email    guilherme.nomeinvalido@email.com
    E informa a senha    123456
    Quando clicar em Cadastrar
    Então o sistema deve apresentar mensagem na tela de cadastro    Nome deve ter pelo menos 3 caracteres

CT03 - Deve exibir erro com email inválido
    Dado que o usuário informa o nome    Guilherme Teste
    E informa o email    emailinvalido
    E informa a senha    123456
    Quando clicar em Cadastrar
    Então o sistema deve apresentar mensagem na tela de cadastro    E-mail inválido

CT04 - Deve exibir erro com senha inválida
    Dado que o usuário informa o nome    Guilherme Teste
    E informa o email    guilherme.senhainvalida@email.com
    E informa a senha    123
    Quando clicar em Cadastrar
    Então o sistema deve apresentar mensagem na tela de cadastro    Senha deve ter pelo menos 6 caracteres

*** Keywords ***

Abrir navegador na tela de cadastro
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Click Link    ${LINK_CADASTRO}
    Wait Until Element Is Visible    ${INPUT_NOME}    timeout=10s

Garantir tela de cadastro
    Go To    ${URL}
    Execute JavaScript    localStorage.clear()
    Reload Page
    Wait Until Element Is Visible    ${LINK_CADASTRO}    timeout=10s
    Click Link    ${LINK_CADASTRO}
    Wait Until Element Is Visible    ${INPUT_NOME}    timeout=10s
    Sleep    0.5s

Dado que o usuário informa o nome
    [Arguments]    ${nome}=${EMPTY}
    Execute JavaScript    document.getElementById('signup-nome').value = '${nome}';

E informa o email
    [Arguments]    ${email}=${EMPTY}
    Execute JavaScript    document.getElementById('signup-email').value = '${email}';

E informa a senha
    [Arguments]    ${senha}=${EMPTY}
    Execute JavaScript    document.getElementById('signup-senha').value = '${senha}';

Quando clicar em Cadastrar
    Submit Form    id=form-signup
    Sleep    1s

Então o sistema deve exibir mensagem de cadastro realizado
    Wait Until Element Is Visible    css=#msg-login.show    timeout=8s
    ${texto}=    Get Text    ${MSG_LOGIN}
    Should Be Equal As Strings    ${texto}    Cadastro realizado! Faça login para continuar.

Então o sistema deve apresentar mensagem na tela de cadastro
    [Arguments]    ${mensagem_esperada}
    Wait Until Element Is Visible    css=#msg-signup.show    timeout=8s
    ${texto}=    Get Text    ${MSG_SIGNUP}
    Should Be Equal As Strings    ${texto}    ${mensagem_esperada}

Fechar navegador
    Close Browser