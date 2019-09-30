FROM centos

#EXPORT = set variable
#EXPORT DOCKER_BUILDKIT=1
#echo $DOCKER_BUILDKIT

# update and install wget
RUN yum update -y && yum install -y wget

# wget save to the last
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# -p = prefix; -b = bash mode
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh

COPY conda_requirements.txt .
COPY pip_requirements.txt .

ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda
RUN conda install -y --file conda_requirements.txt
RUN pip install -r pip_requirements.txt
RUN conda install -c anaconda psycopg2
RUN conda install -c conda-forge jupyter_contrib_nbextensions

EXPOSE 8889

WORKDIR /usr/src

# hash password = 1234
# from notebook.auth import passwd
# passwd()

ENTRYPOINT [ "jupyter", "lab", "--ip='*'","--port=8889", "--no-browser","--NotebookApp.token=''", "--NotebookApp.password='sha1:a60aa670ae56:dd1afbc5d9585af67965bc9fe187f315ae31f3d8'", "--allow-root" ]