Trigo – DevOps Assignment - Configurations

General:

Please Clone the following repo: https://github.com/trigodevops/test_repo.git

Please work only on that repo – you got all the permissions that you need.

You got 3 hours.

Stage 1:

Please deploy a multi env configuration solution.

You can deploy it anywhere you want with any tool that to want to use.

```http://service_name:8080/prod/service-a/config - will present production configuration of service a 
   http://service_name:8080/prod/service-b/config - will present production configuration of service b
   http://service_name:8080/dev/service-a/config  - will present dev configuration of service a
```

Stage 2:

Update app version and deploy. (to dev and then to prod)
Update configuration values and deploy. (Update one of the values in the config file - should restart the app and as a result to update the link)
