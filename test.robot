*** Settings ***
Documentation   Verify that Visual Studio Code can navigate between Robot files
Library         BuiltIn
Resource        test.resource

*** Test Cases ***

Sample Test
    Create Once
    Create Multiple Times
    ${pageContent}    Load Webpage    https://google.com
    Log To Console    ${pageContent}