Trigo – DevOps Assignment - Configurations

General:

Please Clone the following repo: https://github.com/trigodevops/test_repo.git

Please work only on that repo – you got all the permissions that you need.

You got 3 hours.

Stage 1:

Please deploy a multi env configuration solution

You can deploy it anywhere you want with any tool that to want to use.

This are the 3 Links - Please notice - 

a. 2 Different services.
b. Dont copy the config to the app - inject it.

1. http://service_name:8080/prod/service-a/config - will present production configuration of service a 

2. http://service_name:8080/prod/service-b/config - will present production configuration of service b

3. http://service_name:8080/dev/service-a/config  - will present dev configuration of service a

Stage 2:

1. Update app version and deploy. (to dev and then to prod)
2. Update configuration values and deploy. (Update one of the values in the config file - should restart the app and as a result to update the link)
