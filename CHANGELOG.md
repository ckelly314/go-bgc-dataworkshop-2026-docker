# GO-BGC Data Workshop 2026 Docker Image Changelog

All notable changes to the JupyterHub Docker image will be documented here. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.9.8] - 2026-08-11

### Added

- Added /home/jovyan/.local/bin to PATH
- Added installation of aws cli to Dockerfile
- Added boto3, r-paws, and r-aws.s3 to conda-packages.txt


## [0.9.7] - 2026-08-09

### Added

- Added litellm to conda-packages.txt
- Added npm-packages.txt to install npm pacakges for copilot and claude agents for jupyter-ai

### Changed

- Upgrade node version pin to >=22

## [0.9.6] - 2026-08-08

### Added

- Now use repo2docker-action to build docker image via GitHub action

### Removed

- Removed the jupyter-ai-jupyternaut package from pip-packages.txt

### Fixed

- Fixed the content of CHANGELOG.md
- Fixed the content of VERSION


## [0.9.5] - 2026-08-06

### Fixed

- Pinned version of erddapy to <3.3 in conda-packages.txt to avoid conflicts with argopy


## [0.9.4] - 2026-08-06

### Added 

- Added the parcels and ipympl to conda-packages.txt


## [0.9.3] - 2026-08-05

### Added

- Based on quay.io/jupyter/r-notebook:hub-5.4.6
- Updated RStutio to version 2026.07.1-147
- Initial release.