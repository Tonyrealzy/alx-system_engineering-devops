## Server requests failure report
A month ago, it was reported that the platform was returning '500 Error' on all requests made on the platform routes, all the services were down.  90% of users were affected. The root cause was the failure of our master server web-01.

## Timeline
The error was realized on Saturday 6th May, 1000 hours (West Africa Time) when Mr Swill saw the master server lagging in speed. Our engineers on call disconnected the master server web-01 for further system analysis and channelled all requests to client server web-02. They solved the problem by Sunday 7th May 2200 hours (West Africa Time).

## Cause and resolution
The platform is served by 2 ubuntu cloud servers. The master server web-01 was connected to serve all requests but it stopped functioning due to memory outage. This is probably as a result of so many requests because during a previous test, the client server web-02 was disconnected temporarily for testing and was not reconnected to the load balancer afterwards. 


The issue was fixed when the master server was temporarily disconnected for memory clean-up and then reconnected to the loadbalancer. Then, round-robin algorithm was configured so that both the master and client servers can handle equal amount of requests.

## Prevention against such problem in future
- Choose the best loadbalancing algorithm for your programs
- Always keep an eye on your servers to ensure they are running properly
- Have extra back-up servers to prevent your program from completely going offline during an issue