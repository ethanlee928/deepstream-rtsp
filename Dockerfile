FROM nvcr.io/nvidia/deepstream:6.1.1-samples

ENV TZ=Asia/Hong_Kong
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN apt-get install -y git wget libcairo2-dev

RUN apt-get install python3-pip python3-gi python3-numpy \ 
    libgstrtspserver-1.0-0 gir1.2-gst-rtsp-server-1.0 \
    v4l-utils vim unzip curl -y

RUN pip3 install pyyaml overrides

ENV PYDS_VER=1.1.4
ENV PYDS=x86_64

RUN wget https://github.com/NVIDIA-AI-IOT/deepstream_python_apps/releases/download/v${PYDS_VER}/pyds-${PYDS_VER}-py3-none-linux_${PYDS}.whl
RUN pip3 install pyds-${PYDS_VER}-py3-none-linux_${PYDS}.whl && rm pyds-${PYDS_VER}-py3-none-linux_${PYDS}.whl
