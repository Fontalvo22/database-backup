FROM python:3.14.0a1-bookworm

WORKDIR /app

COPY .aws /root/.aws

COPY . .

RUN pip install -r requirements.txt

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# for allow exports mongodb, mysql and postgresql

RUN apt-get update && \
    wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-debian92-x86_64-100.3.1.deb && \
    apt install -y --no-install-recommends ./mongodb-database-tools-*.deb && \
    apt-get install -y --no-install-recommends default-mysql-client postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f mongodb-database-tools-*.deb

# aws cli
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN ./aws/install
# RUN aws configure
RUN apt-get install mongodb-database-tools
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
