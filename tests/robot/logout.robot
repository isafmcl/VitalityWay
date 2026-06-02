*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://localhost:3000

*** Test Cases ***
Realizar Logoff Com Sucesso

    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Input Text    id=login-email    admin@email.com
    Input Text    id=login-senha    admin123

    Click Button    Entrar

    Sleep    2s

    Click Button    id=btn-logout

    Sleep    2s

    Page Should Contain Element    id=login-email

    Capture Page Screenshot

    Close Browser