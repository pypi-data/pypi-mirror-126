# SSL Metrics Badges

> Convert PNG graphs into GitHub compatable badges

[![Publish to PyPi](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-badges/actions/workflows/pypi.yml/badge.svg)](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-badges/actions/workflows/pypi.yml)

![Example](tests/badge.svg)

## Table of Contents

- [SSL Metrics Badges](#ssl-metrics-badges)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Install](#how-to-install)
  - [How to Run](#how-to-run)
    - [Note on Colors](#note-on-colors)

## About

A script to convert graphs (or other `.png` files 😉) into GitHub compatible `.svg` badges.

### Who is this application for?

This application is meant to be used by developers who want a badge that displays graphical information.

It can also be used as an interface into the [pybadges](https://github.com/google/pybadges) project.

### Credits

[Software and Systems Laboratory](https://github.com/SoftwareSystemsLaboratory)

## How to Install

0. Install `Python 3.9.6 +`
1. `pip install ssl-metrics-badges`

## How to Run

0. `ssl-metrics-badges -h` to view the command line arguements
1. `ssl-metrics-badges --g GRAPH.png -lc COLOR -lt "LEFT TEXT" -u URL -o FILE.svg -rt "RIGHT TEXT" -rc COLOR -t TITLE`

### Note on Colors

Colors can either be phonetically called (such as **red**, **blue**, or **green**) or through hex codes (#123456).
