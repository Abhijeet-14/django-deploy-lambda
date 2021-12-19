# Django deploy - AWS Lambda + API Gateway with ZAPPA

1. API Gateway ??

   > - fully managed service
   > - create, publish, maintain, monitor & secure APIs to scale
   > - RESTful APIs and WebSocket APIs

2. Zappa

   > - Request comes into API Gateway
   > - Gateway fires up a server inside a Lambda function
   > - server is then fed the request
   > - Handled by django-app thro WSGI layer

3. goto AWS IAM
4. users > 'add users'
5. give username
6. choose 'Programmatic access' > NEXT permissions > NEXT tag > NEXT Users
7. click 'create user'
   > successfully created user
8. download access-key & secret-access-key
9. to create new access-key -> goto security-credentials -> Access key -> click 'create access key'
10. pip install zappa
11. intsall awscli
12. run 'aws configure' - to configure aws with access key
13. put 'access key' -> 'secret key' -> region -> output format (json)
14. now give permission to this user which ZAPPA & we need
15. 'add permission' -> 'create group' -> 'create policy' -> json -> add policy json

16. give name to this permission group -> 'create policy'

17. give 3 permissions

    - django_lambda_zappa_execution ['https://medium.com/@gautamborgohain/setting-up-aws-roles-and-policies-for-lambda-apps-using-zappa-f943b2d627ae']
    - zappa-django ['https://medium.com/@gautamborgohain/setting-up-aws-roles-and-policies-for-lambda-apps-using-zappa-f943b2d627ae']
    - IAMFullAccess (we can remove thi after deployment)

18. goto IAM user -> add permission -> attach existing policy
19. search for 'permission group by name (e.g., zappa-django)'
20. NEXT > 'Add permission'
21. now create role
22. roles > 'create role' > AWS service > lambda -> NEXT -> choose policies -> NEXT -> name role -> NEXT

23. NOW goto VSCODE 
24. zappa init -> choose env variable (dev, stagin, production) -> choose profiles (default, AWS1)
26. next zappa will upload DJANGO-APP to private S3 bucket... choose bucket name or default
27. choose settings file
28. deploy globally ? -> n
29. review final config -> and press y
30. created a file zappa_settings.json
31. zappa deploy dev

SUCCESSFULLY DEPLOYED... 

32. ERROR: Warning! Status check on the deployed lambda failed. A GET request to '/' yielded a 502 response code.
    - what happen here is .. zappa wasn't able to upload the django-applicatio to S3. S3 bucket is empty
33. 'zappa tail' to find error stack
    - saying to update SQLlite... let comment database connect in settings.py

34. zappa update dev

35. goto settings.py -> allowed host -> add domain without https 
36. zappa update dev