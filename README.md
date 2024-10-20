<p float="left">
  <img src="/Pictures/prometheus_logo.png" height="85" />
  <img src="/Pictures/GreenCell_logo.jpg" height="85" />
  <img src="/Pictures/fastapi_logo.png" height="85" />
  <img src="/Pictures/docker_logo.png" height="85" />
</p>

# GreenCell_exporter

[![CodeQL](https://github.com/HornaHomeLab/GreenCell_exporter/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/HornaHomeLab/GreenCell_exporter/actions/workflows/github-code-scanning/codeql)
[![CI/CD](https://github.com/HornaHomeLab/GreenCell_exporter/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/HornaHomeLab/GreenCell_exporter/actions/workflows/ci-cd.yml)

##### version: 0.0.2

Prometheus Exporter for [GreenCell UPS APP](https://gcups.greencell.global/en)

It is containerized FastAPI based application to expose UPS metrics provided by GC UPS APP.

GC APP is queried when `/metrics` endpoint is accessed,
which means that if the exporter is not in use it do not generate traffic.

## Sample Grafana dashboard

Dashboard is available for import [here](/Grafana/Dashboards/)

### UPS

![image](/Grafana/Pictures/UPS_1.png)

## How to run

1. Create the `.env` file to provide necessary values specified in [Parameters](#parameters) section.
2. Build docker image using `docker compose build`
3. Start docker compose using `docker compose up -d`
4. Metrics will be available at `http://<your_hostname>:51772/metrics`

> [!IMPORTANT]
> `.env` file filled with data from table should be saved in `./app` directory before building docker image.

### Parameters

| Name              | Description                                       |
| ----------------- | ------------------------------------------------- |
| `GC_PASSWORD`     | Password to log in to GC remote access panel.     |
| `GC_APP_IP`       | IP address of host which is running GC APP.       |
| `GC_APP_PORT`     | Port on which GC APP is accessible                |
| `GC_APP_PROTOCOL` | Protocol used to access GC APP (`http` / `https`) |
