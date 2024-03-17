---
title: "Automated Acceptance Test Procedure"
date: 2024-03-07T17:13:18+02:00
type: "page"
draft: true
description: "Develop the infrastructure to run black box tests on CI/CD and provide a stable development environment"
order: 1
---

# Automated Acceptance Testing Procedure (AATP)

## Overview
Software moves fast and ensuring service level agreement and user satisfaction
can be challenging. This engagement is designed to meet these challenges head-on,
developing a stable automation infrastructure to function as a gatekeeper preeventing bugs from reaching production and finding them before they are merged.

## Solution

A tailor-made well-documented test automation infrastructure that aligns
with your specific infrastructure and requirements. This infrastructure will be
programmed to run black box tests on CI pipeline and provide a stable development environment.
Batteries included:

- Simple bash scripts to run the tests
- Docker compose to setup the virtual lab
- Playwright to run the tests
- WireMock to mock external services
- MailHog to capture and inspect emails
- Custom mocks that emulate the environment required by the component under test
- End-to-end testing suite that covers the happy flow of the application
- Comprehensive documentation and training
- Mentoring a team member to maintain and extend the infrastructure

## Benefits

- Reduce the number of bugs reaching production
- Increase the confidence in the codebase
- Eliminate the need for manual testing
- Foster a culture of quality and innovation
- Empower your team with new skills and knowledge

## Implementation Plan
The roll-out of the Automated Acceptance Testing Procedure will be phased as follows:

1. Requirements Gathering: Interview developers, testers and stakeholders to define and document infrastructure's usage scenarios
2. Design & Architect: Design the automation infrastructure to serve as gatekeeper based on your technology stack and scenarios
3. Happy flow testing suite: A simple happy flow test suite to test the infrastructure
4. Setup the virtual lab: Add the scripts, configuration files and directory
tree that emulate the environment required by the component under test and runs the tests
4. CI Integration: Integrate the happy flow test suite into your CI pipeline to ensure only tested code is merged
5. Training: Provide comprehensive training and documentation for the team to smooth adoption


*If you ready or think you're ready for this quest* [let's talk]({{< letsTalk >}}).
