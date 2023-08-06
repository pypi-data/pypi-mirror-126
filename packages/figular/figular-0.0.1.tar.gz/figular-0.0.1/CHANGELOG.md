<!--
SPDX-FileCopyrightText: 2021 Galagic Limited, et. al. <https://galagic.com>

SPDX-License-Identifier: CC-BY-SA-4.0

figular generates visualisations from flexible, reusable parts

For full copyright information see the AUTHORS file at the top-level
directory of this distribution or at
[AUTHORS](https://gitlab.com/thegalagic/figular/AUTHORS.md)

This work is licensed under the Creative Commons Attribution 4.0 International
License. You should have received a copy of the license along with this work.
If not, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
-->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.1 - 2021-11-08](https://gitlab.com/thegalagic/figular/-/releases/v0.0.1)

### Added

* New cmdline flag `--help` to show usage.
* An API using FastAPI so Figular can be hosted and accessible over HTTP.
* GOVERNANCE.md was missing, added benevolent dictator.

### Fixed

* Bugs in figure `concept/circle`:
  * Crash when not given any blobs. Now we will skip drawing.
  * Crash when one blob and middle=true
  * Blobs were drawn on top of each other when only two blobs and middle=true

## [0.0.0 - 2020-04-01](https://gitlab.com/thegalagic/figular/-/releases/v0.0.0)

First version, basic cmdline usage and docs.

### Added

* New figure `concept/circle`, see docs for details.
