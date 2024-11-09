FROM nvidia/cuda:11.6.1-cudnn8-devel-ubuntu20.04
ARG CUDA_VERSION=11.6.1
ARG CUDNN_VERSION=8
ARG PYTHON_VERSION=3.8
SHELL ["/bin/bash", "-c"]
RUN export DEBIAN_FRONTEND=noninteractive && \
    CUDA_PATH=(/usr/local/cuda-*) && \
    CUDA=`basename $CUDA_PATH` && \
    echo "$CUDA_PATH/compat" >> /etc/ld.so.conf.d/${CUDA/./-}.conf && \
    ldconfig && \
    # Install all dependencies for OpenCV
    apt-get -y update -qq --fix-missing && \
    apt-get -y install --no-install-recommends \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-dev \
        python-setuptools \
        python3-setuptools \
        $( [ ${PYTHON_VERSION%%.*} -ge 3 ] && echo "python${PYTHON_VERSION%%.*}-distutils" ) \
        git \
        wget \
        unzip \
        cmake \
    && \
    # install python dependencies
    sysctl -w net.ipv4.ip_forward=1 && \
    wget https://bootstrap.pypa.io/get-pip.py --progress=bar:force:noscroll && \
    python${PYTHON_VERSION} get-pip.py && \
    rm get-pip.py

RUN apt-get update -y
RUN apt-get install -y python3-dev python3-setuptools libboost-all-dev libblas-dev liblapack-dev libatlas-base-dev
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0

RUN git clone https://github.com/davisking/dlib.git && \
    cd dlib && \
    mkdir build && cd build && \
    cmake -DCUDA_HOST_COMPILER=/usr/bin/gcc-7 -DCMAKE_PREFIX_PATH=/usr/lib/x86_64-linux-gnu/ -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1 .. && \
    cmake --build . --config Release && \
    ldconfig
    #make install 

RUN cd dlib && \
    python3 setup.py install

RUN python3 -m pip install opencv-python==4.8.0.74