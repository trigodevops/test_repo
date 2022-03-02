## Trigo – DevOps Assignment -Shayel's Solution
#Stage 1:

### How to Run:
 
1. Due to computing issues you will have to clone the code to your computer 
2. build the image locally using the included Dockerfile
3. upload it to any container registry you desire
4. create new deployment and **mount** the config files to `config` folder(in case of forget to mount it will use the default values which currently exists in the files):
   * base_config - will be retrieved once at the begging of the program.
   * prod_config - will be retrieved each time the client access the prod endpoint
   * dev_config - will be retrieved each time the client access the dev endpoint
   * app_config - this config file used to define paramters for running the app (port,routes etc.)

5. after you deployed the image 2 times (once for service-a other one for service-b) use the included file **ingress.yaml** to deploy the ingress which expose endpoint according to the requirements:
###Supported Endpoints:
By review the ingress.yaml you can see that there are 3 endpoints exposed:
   1. /dev/service-a/config 
      a. return base config and dev config of service a
   2. /prod/service-a/config
      a. return base config and prod config of service a
   3. /prod/service-b/config
      a. return base config and prod config of service b
      
####thougths:
1. During coding, I thought about implement a class for config as below:
    * Separate file for each config type and read it when the customer access the endpoint
    * implement Class for Base config and inherit from it to Dev and Prod Classes.
    * store the config in DB and retrieve based on requirements.
#Stage 2:
1. the required process is CI/CD tool which we define with the following steps:
    1. for merging into specific (dev) branch, it should accomplish necessary tests for the products
    2. create image with `dev` tag
    3. redeploy the exists workload in the dev env (not sure about the CD flow)
2. consider to create a listener program that will watch for changes in the config map,once it changes the program will restart the pod". another solution to this issue can be to load the config map each X seconds so the new configuration will be load to the pod every time it "refreshed"