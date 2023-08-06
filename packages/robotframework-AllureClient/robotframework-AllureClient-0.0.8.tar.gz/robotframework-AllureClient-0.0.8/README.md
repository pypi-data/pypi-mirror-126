# robotframework allure client


## Introduction

Robot framework client library for allure docker service  (http://47.114.163.85/swagger/allure-docker-service/).

## Installation

The recommended installation method is using pip::

    pip install robotframework-AllureClient

Usage
-----

.. code:: robotframework

*** Settings ***
Library    AllureClient    http://47.114.163.85/swagger/allure-docker-service
*** Test Cases ***
test 1
    Get allure version
test 2
    Get swagger API doc
test 3
    Get Swagger API Specification
test 4
    Get Allure config
test 5
    Get latest report    test
test 6
    Send results files    test    true    output\\allure
test 7
    Generate new report    test
test 8
    Clean history    test
test 9
    ​Clean results    test
test 10
    ​Export emailable Allure report    test    \\result
test 11
    ​Render emailable Allure report    test
test 12
    ​Export Allure report    test
test 13
    ​Get all projects
test 14
    ​Create a new project    test1
    ​Create a new project    test2
    ​Create a new project    test3
test 15
    ​Search projects    test3
test 16
    ​Get an existent project    sample
test 17
    ​Delete an existent project    test1
    ​Delete an existent project    test2
    ​Delete an existent project    test3

test 18
    ​Get reports    sample    1    true