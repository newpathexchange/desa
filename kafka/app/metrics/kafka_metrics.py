from jmxquery import JMXConnection, JMXQuery
from time import sleep

jmx_port = 9111
brokers = [ 'desa1', 'desa2', 'desa3' ]

jmx_connections = []
for broker in brokers:
  jmx_connections.append(JMXConnection(f"service:jmx:rmi:///jndi/rmi://{broker}:{jmx_port}/jmxrmi"))

jmx_query = [
  JMXQuery("kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec/OneMinuteRate"),
  JMXQuery("kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec/OneMinuteRate"),
  JMXQuery("kafka.server:type=BrokerTopicMetrics,name=TotalProduceRequestsPerSec/OneMinuteRate"),
  JMXQuery("kafka.server:type=BrokerTopicMetrics,name=TotalFetchRequestsPerSec/OneMinuteRate"),
  JMXQuery("kafka.network:type=RequestMetrics,name=TotalTimeMs,request=Produce/999thPercentile"),
  JMXQuery("kafka.network:type=RequestMetrics,name=TotalTimeMs,request=FetchConsumer/999thPercentile"),
]

while True:
  #for con in jmx_connections:
  print('=' * 80)
  print(f"{'broker':<8}{'BytesIn':^12}{'MessagesIn':^12}{'ProduceReqs':^12}{'FetchReqs':^12}{'ProduceMS':^12}{'ConsumerMS':^12}")
  print('-' * 80)
  sample = []
  for i in range(len(brokers)):
    sample.append([])
    con = jmx_connections[i]
    metrics = con.query(jmx_query)
    for metric in metrics:
      sample[i].append(round(metric.value,2))

    print(f"{brokers[i]:<8}{sample[i][0]:>12.2f}{sample[i][1]:>12.2f}{sample[i][2]:>12.2f}{sample[i][3]:>12.2f}{sample[i][4]:>12.2f}{sample[i][5]:>12.2f}")

  print('-' * 80)
  s = [round(sum(l),2) for l in zip(*sample)]
  a = [round(sum(l)/len(l),2) for l in zip(*sample)]
  print(f"{'':<8}{s[0]:>12.2f}{s[1]:>12.2f}{s[2]:>12.2f}{s[3]:>12.2f}{a[4]:>12.2f}{a[5]:>12.2f}")

  sleep(10)



