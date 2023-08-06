# SECTOOL

A tool for keeping secrets during software builds and deployments.

## Challenge
The secrets like API keys or passwords should be used during run time and provided by execution environment.
The simple solution is keeping them as environment variables. But values of the variables are usually kept as
plain text inside files like ``Dockerfile`` or ``docker-compose.yml`` which is not secure.

## Way to solve
The tool solves the issue, it allows you to keep secrets in an encrypted file and inject the values
during software builds.

### How it works?
1. You create an .ini file where in section ``secrets`` you keep all your secrets.
2. Encrypt the file. Later you can use the file (or files if you need different secrets for different environments).
3. Run ``sectool`` by specifying the file and your deployment config file. The tool reads your 
deployment config, injects the corresponding values and print the result to stdout.
4. Here is the step when Linux magic begins, the stdout can be piped to your building or deployment tool,
also ``xargs`` can help.

### Examples
Inject to ``Dockerfile`` and build a Docker image:
```shell
echo -n "Enter your password: "
read PASSWORD
python3.7 sectool.py secrets.dat $PASSWORD Dockerfile | docker build -t tulip -f - .
```

Inject to ``docker-compose.yml`` and build all images mentioned there:
```shell
echo -n "Enter your password: "
read PASSWORD
python3.7 sectool.py secrets.dat $PASSWORD docker-compose.yml | docker-compose -f - build
```

Inject to AWS Task Definition:
```shell
echo -n "Enter your password: "
read PASSWORD
python3.7 sectool.py secrets.dat $PASSWORD my-aws-task-def.json | xargs -0 aws ecs register-task-definition --region eu-west-1 --cli-input-json
```

### How do I encrypt .ini file?
Easy. You need ``openssl``, the software is very popular and included in almost popular Linux/Unix distributions.

How do I encrypt file?
```shell
openssl enc -aes-256-cbc -in secrets.ini -out secrets.dat
```
Don't forget password that the tool will ask! If you forget it, you won't be able to get access to your secrets.

How do I decrypt to check if everything okay?
```shell
openssl enc -aes-256-cbc -k <password> -d -in secrets.dat
```

### How do I mention secret variables in my, for instance, Dockerfile?
Just use a name of the variable in double curly brackets ``{{api_key}}``

Example of .ini file:
```ini
[secrets]
api_key = AGTDBLWLB5BGG7NNVHV
```

Example of Dockerfile:
```dockerfile
FROM ubuntu:20.04
USER wheel

ENV API_KEY={{api_key}}
```
