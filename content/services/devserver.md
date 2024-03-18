---
title: "Shared Development Server"
date: 2024-03-12T09:14:11+02:00
type: "page"
description: "Cutting costs and unifying devs' envs by setting up a shared development server"
order: 2
---


## Overview
This proposal outlines a strategic initiative to transition your software development environment to a cloud-hosted development server. This move is designed to significantly reduce hardware costs, improve developer productivity and foster collaboration. Not only will this eliminate "it works on my machine" issues, but it will also enable practices such as pair programming and catching bugs as soon as they are written.


## Solution
Configure and install a server to serve as a shared development environment. The environment will be tailored to the team's needs and will include all the tools and configurations required to develop, test and deploy the software.
Each developer will have a user account on the server simplifying the onboarding process and ensuring that all developers share the same environment.

## Benefits
* Cost Reduction:  CPUs are both expensive and underutilized. Devs’ spend most of their time reading code and docs and sharing a central CPU will increase utilization. This will lower laptops’ specs (chromebooks and tablets become viable options) and extend the lifespan of existing hardware
* Lower **Dev**Ops maintenance:  Maintain one computer instead of one per dev
* Smoother onboarding: No need to install OS dependencies and tools or update dotfiles
* Improved tool chest: Curating the tools and configuration files based on the sudoers’ wisdom.
* Improved Collaboration: Enable pair programming and foster a collaborative development culture.


## Implementation Plan
We start by electing the first team to migrate to a shared server. Once a team is chosen we will:

1. Identify and group the sudoers
2. Research of current tools and configurations
3. Augment the current tool chest and configs with state-of-the art tools
4. Setup up a server and test it
5. Help the devs migrate to the new server
6. Lead pair programming workshops to break the ice


If you ready or think you're ready for this quest [let's talk](https://calendly.com/bennydaon).
