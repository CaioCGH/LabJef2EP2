FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
ARG SHELL=/bin/bash 
RUN apt-get update
RUN apt-get install -y postgresql postgresql-server-dev-10 postgresql-plpython3-10 python3-psycopg2 python3-pip libpq5 antlr4 libssl1.0-dev libkrb5-dev vim git sudo screen

RUN pip3 install antlr4-python3-runtime
RUN sed -i -e '/^local/s/peer/trust/' /etc/postgresql/10/main/pg_hba.conf

RUN echo "sleep 1" >> /etc/bash.bashrc
RUN echo "/etc/init.d/postgresql start" >> /etc/bash.bashrc
RUN echo 'clear \n \
    if [ $COLUMNS -ge 45 ]; then \n\
        echo "********************************************" \n\
        echo "*                                          *" \n\
        echo "* Welcome to WED-SQL execution environment *" \n\
        echo "*                                          *" \n\
        echo "********************************************" \n\
    fi' >> /root/.bashrc

RUN echo 'echo "Updating WED-SQL from remote repository"' >> /root/.bashrc
RUN echo "cd wed-sql && git pull && cd .." >> /root/.bashrc

WORKDIR /bin
RUN ln -sfn bash sh

WORKDIR /root

RUN git clone https://gitlab.com/nhabongo/wed-sql
RUN echo "#!/bin/bash \n\n python3 wed-sql/wsql/wsql.py" > /usr/local/bin/wsql
RUN chmod +x /usr/local/bin/wsql

WORKDIR /root/wed-sql/pg_background

RUN make && make install && make clean

RUN /etc/init.d/postgresql start &&\
	psql -U postgres -d template1 -c 'CREATE EXTENSION plpython3u; CREATE EXTENSION pg_background'

WORKDIR /root

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

CMD ["/bin/bash"]
