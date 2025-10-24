FROM python:3.14

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Install MongoDB tools, MySQL client, PostgreSQL client, and cron
RUN apt-get update && \
    wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-debian92-x86_64-100.3.1.deb && \
    apt install -y --no-install-recommends ./mongodb-database-tools-*.deb && \
    apt-get install -y --no-install-recommends default-mysql-client postgresql-client cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f mongodb-database-tools-*.deb

# Install AWS CLI
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
#     unzip awscliv2.zip && \
#     ./aws/install && \
#     rm -rf awscliv2.zip aws

# Copy AWS configuration files
COPY .aws /root/.aws

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh


CMD [ "tail", "-f", "/dev/null" ]