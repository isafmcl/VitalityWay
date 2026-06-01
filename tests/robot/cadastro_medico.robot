*** Settings ***
Library    SeleniumLibrary

Suite Setup       Fazer login e acessar tela de médicos
Suite Teardown    Fechar navegador
Test Setup        Garantir tela de médicos

*** Variables ***
${URL}              http://localhost:3000
${BROWSER}          chrome
${INPUT_EMAIL}      id=login-email
${INPUT_SENHA}      id=login-senha
${BTN_LOGIN}        css=#form-login button[type=submit]
${INPUT_NOME}       id=med-nome
${INPUT_CRM}        id=med-crm
${SEL_ESP}          id=med-esp
${BTN_CADASTRAR}    css=#form-medico button[type=submit]
${MSG}              id=msg-medico

*** Test Cases ***

CT01 - Deve cadastrar médico com dados válidos
    Dado que o usuário informa o nome do médico    Dr Robot Guilherme Dois
    E informa o CRM    8888888
    E seleciona a especialidade    e1
    Quando clicar em Cadastrar Médico
    Então o sistema deve apresentar a mensagem    Médico cadastrado com sucesso

*** Keywords ***

Fazer login e acessar tela de médicos
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${INPUT_EMAIL}    timeout=10s
    Input Text      ${INPUT_EMAIL}    cuidador@email.com
    Input Password  ${INPUT_SENHA}    12345678
    Click Button    ${BTN_LOGIN}
    Sleep    2s
    Execute JavaScript    navigateTo('medicos')
    Sleep    3s
    Wait Until Element Is Visible    ${INPUT_NOME}    timeout=10s

Garantir tela de médicos
    Execute JavaScript    navigateTo('medicos')
    Sleep    1s
    Wait Until Element Is Visible    ${INPUT_NOME}    timeout=10s

Dado que o usuário informa o nome do médico
    [Arguments]    ${nome}=${EMPTY}
    Clear Element Text    ${INPUT_NOME}
    Input Text    ${INPUT_NOME}    ${nome}

E informa o CRM
    [Arguments]    ${crm}=${EMPTY}
    Clear Element Text    ${INPUT_CRM}
    Input Text    ${INPUT_CRM}    ${crm}

E seleciona a especialidade
    [Arguments]    ${especialidade_id}
    Select From List By Value    ${SEL_ESP}    ${especialidade_id}

Quando clicar em Cadastrar Médico
    Click Button    ${BTN_CADASTRAR}
    Sleep    1s

Então o sistema deve apresentar a mensagem
    [Arguments]    ${mensagem_esperada}
    Wait Until Element Is Visible    css=#msg-medico.show    timeout=8s
    ${texto}=    Get Text    ${MSG}
    Should Be Equal As Strings    ${texto}    ${mensagem_esperada}

Fechar navegador
    Close Browser