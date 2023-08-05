# gherlint
Linter for Gherkin feature files, written in Python

## Install
Simply run ``pip install gherlint``.

## Linting Feature Files
``gherlint`` comes with a command line interface.
To recursively lint all feature files in a directory, run ``gherlint lint``.

## Computing Metrics
``gherlint`` can also create some metrics for you if you want to know how many features, scenarios and steps you have
in your test suite. To do so, run ``gherlint stats``.

## Disclaimer
``gherlint`` is still in an early development phase. New checks will be added over time.
If you want to contribute, feel free to open issues suggesting useful checkers, or open a pull request if you want
to!

## Roadmap

The following work items are planned for the upcoming releases:

* V0.0.x - V0.1.0:
    * Parser and object model for feature files
    * Basic checkers to demonstrate workflow
    * Basic text based reporter
* V0.1.x - V1.0: **<-- we are here**
    * Add more checkers
    * Add more output formats
    * Extend object model as necessary for checkers
    * Reach a stable interface for object model, checkers and reporters
* V1.x - V2.0:
    * Support configuration to enable/disable individual messages
    * Implement plugin architecture to allow users to add custom checkers
# CHANGELOG

## V0.4.0
New checks:
* ``unused-parameter``
* ``empty-background``
* ``outline-could-be-a-scenario``
* ``consider-using-background``
* ``examples-outside-scenario-outline``
* ``duplicated-tag``

Other changes:
* ``unparseable-file`` is now issued for all nodes that offend the ``gherkin`` parser together with more error information provided by it
* ``missing-parameter`` now clearly states what parameter is not defined in the examples
* If ``gherlint`` patches the file contents with a forgotten ``# language`` tag the line numbers for messages
are no longer shifted
* Types of ``And`` and ``But`` steps are now inferred correctly
* New command ``fix-language-tags`` to automatically add or fix missing or incorrect language tags
* Rename some message codes to have a defined structure: each checker has its own hundreds digit.

## V0.3.0
New checks:
* ``missing-language-tag``
* ``wrong-language-tag``
* ``unparseable-file``

Other changes:
* ``gherlint`` can now automatically detect the language used and make sure that it can parse the files
even without a ``# language`` token present.

## V0.2.0
New checks:
* ``missing-given-step``
* ``missing-when-step``
* ``missing-then-step``
* ``empty-scenario``
* ``empty-feature``
* ``file-has-no-feature``
* ``missing-parameter``

Other changes:
* Support for ``Background``
* Determination of step type independent of language
* Distinction between ``Scenario`` and ``Scenario Outline`` independent of language

## V0.1.0
First package in alpha status:
* Parser and object model for feature files
* Basic checkers to demonstrate workflow
* Basic text based reporter
