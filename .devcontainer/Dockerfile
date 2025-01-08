# ARG VARIANT="3"
# FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ARG CUDA_VERSION="11.1.1"
ARG UBUNTU_VERSION="20.04"
FROM nvidia/cuda:${CUDA_VERSION}-devel-ubuntu${UBUNTU_VERSION}

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y git \
    && apt-get install -y wget \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update -y \
    && apt-get install -y htop \
    && apt-get install -y tmux \
    && apt-get install -y vim \
    && apt-get install -y cron \
    && apt-get install -y acl
    
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 