# Kafka Architect Exercise

The solution includes several areas of code files:
  * Terraform files used to build VMWare VMs for the solution (for reference only)
  * Ansible playbooks to build ZooKeeper ensemble, Kafka cluster, and Schema Registry
  * Kafka applicaiton files to generate and measure load on the Kafka cluster
    * Ansible playbook to create Kafka topic
    * Rate limited producer of fake data and consumer
    * Simple script to dump Kafka metrics to a terminal
    * Kubernetes deployment and Docker build

Ansible playbooks execution (saomple output in the PDF)
```
cd kafka/ansible
ansible-playbook -i env/desa zk-ensemble.yaml
ansible-playbook -i env/desa kafka-cluster.yaml
ansible-playbook -i env/desa schema-registry.yaml
```

Kafka topic creation (sample output in the PDF)
```
cd kafka/app/ansible
ansible-playbook -i "desa1," -e "ansible_user=npxlab" kafka-topic.yaml
```

Kubernetes setup (sample output of Docker builds in the PDF)
```
cd kafka/app/producer
./docker_build.sh v0.1.1
cd ../consumer
./docker_build.sh v0.1.1
cd ../k8s
./deploy_desa_producer.sh
./deploy_desa_consumer.sh
```

Sample output from metrics script
```
paul@oikos-dev:~$ . ~/.venv/jmx/bin/activate
(jmx) paul@oikos-dev:~$ cd kafka/app/metrics
(jmx) paul@oikos-dev:~/code/desa/kafka/app/metrics$ python kafka_metrics.py
================================================================================
broker    BytesIn    MessagesIn ProduceReqs  FetchReqs   ProduceMS   ConsumerMS 
--------------------------------------------------------------------------------
desa1       17589.32        5.70        5.70      154.90       42.00      527.25
desa2       16189.83        5.25        5.25      157.77       52.77      523.36
desa3       15875.30       10.67        5.41      139.81       51.97      502.00
--------------------------------------------------------------------------------
            49654.45       21.62       16.36      452.48       48.91      517.54
================================================================================
broker    BytesIn    MessagesIn ProduceReqs  FetchReqs   ProduceMS   ConsumerMS 
--------------------------------------------------------------------------------
desa1       17828.12        5.78        5.78      156.57       42.00      527.25
desa2       16099.47        5.22        5.22      156.90       52.77      523.36
desa3       16219.73       10.83        5.53      143.31       51.97      502.00
--------------------------------------------------------------------------------
            50147.32       21.83       16.53      456.78       48.91      517.54
[...]
```

### Extra Commands (for reference)

Run Kafka GUI in docker
```
docker run --rm -p 8080:8080 \
	-e KAFKA_CLUSTERS_0_NAME=test \
	-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=desa1:9092 \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_PLAINTEXT \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=SCRAM-SHA-256 \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='org.apache.kafka.common.security.scram.ScramLoginModule required username="admin" password="admin123encryptme";' \
        -e KAFKA_CLUSTERS_0_JMXPORT=9111 \
        -e KAFKA_CLUSTERS_0_JMXSSL=false \
	-d provectuslabs/kafka-ui:latest
```

Kuberenetes commands
```
# Adjust cfgmap settings and redeploy, then
kubectl rollout restart deployment desa-producer-deployment

# View logs of producer or consumer pods
kubectl logs -fl component=producer
kubectl logs -fl component=consumer
```