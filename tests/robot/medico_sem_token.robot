*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://localhost:5000

*** Test Cases ***
Cadastro De Medico Sem Token
    Create Session    api    ${BASE_URL}

    ${body}=    Create Dictionary
    ...    nome=Dr. Carlos Teste
    ...    crm=123456
    ...    especialidadeId=1

    ${resposta}=    POST On Session
    ...    api
    ...    /medicos
    ...    json=${body}
    ...    expected_status=401

    Should Be Equal As Integers    ${resposta.status_code}    401
    ${json}=    Set Variable    ${resposta.json()}
    Should Be Equal    ${json}[codigoErro]    NAO_AUTORIZADO
    Should Be Equal    ${json}[mensagem]    Token inválido ou ausente