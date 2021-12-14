## Trigo – DevOps Assignment

### General:

* Please Clone the following repo: https://github.com/trigodevops/test_repo.git  

* Please work only on that repo (you got all the permissions that you need)

* Please provide a descriptive readme file, so we know how to run your solution

* Solution needs to have the ability to scale

* The assignment is limited to 3 hours

### Stage 1:  
1. Deploy a multi env configuration solution anywhere you want with any tool that to want to use.

2. There are 2 services and 3 Links:

    A. http(s)://ADDRESS:8080/prod/service-a/config - will present production configuration of service a 

    B. http(s)://ADDRESS:8080/prod/service-b/config - will present production configuration of service b

    C. http(s)://ADDRESS:8080/dev/service-a/config  - will present dev configuration of service a

3. Each service will have its own config with accordance to the environment
4. Each service will respond with its config 
5. Don't copy the config to the app - inject it


### Stage 2:
1. Update app version and deploy it to dev and then to prod
2. Update configuration values and deploy (Update one of the values in the config file - should restart the app and as a result to update the service response)
