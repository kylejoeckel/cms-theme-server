# CMS Theme Server

The CMS Theme Server is a serverless application designed to manage themes for a content management system. It provides API endpoints to create, retrieve, update, and delete themes, utilizing AWS Lambda and DynamoDB for efficient and scalable operations.

## Features

- Create, read, update, and delete themes.
- Store themes with unique identifiers and group associations.
- Search for themes by ID or group name.

## Requirements

- Node.js
- Serverless Framework
- AWS CLI
- Python 3.10
- AWS account

## Setup

### Install Dependencies

Install the Serverless Framework globally and other dependencies:

```bash
npm install -g serverless
npm install serverless-offline serverless-dynamodb-local
```

### AWS Configuration

Configure your AWS credentials to allow the Serverless Framework to deploy to your AWS account:

bashCopy code

`aws configure`

Enter your AWS Access Key ID, Secret Access Key, and default region.

Deployment
----------

Deploy the application to AWS:

bashCopy code

`serverless deploy`

This command will set up the AWS Lambda functions, API Gateway endpoints, and DynamoDB table as specified in the `serverless.yml` file.

Usage
-----

### Create Theme

bashCopy code

`curl -X POST https://<api-gateway-url>/themes -d '{"groupName":"default", "theme": {"palette": {"primary": {"main": "#FFD700"}}}}'`

### Retrieve Theme

bashCopy code

`curl https://<api-gateway-url>/themes/{id}`

### Update Theme

bashCopy code

`curl -X PUT https://<api-gateway-url>/themes/{id} -d '{"theme": {"palette": {"primary": {"main": "#000000"}}}}'`

### Delete Theme

bashCopy code

`curl -X DELETE https://<api-gateway-url>/themes/{id}`

Local Development
-----------------

To run the application locally with Serverless Offline and DynamoDB Local:

bashCopy code

`serverless offline start`

This will start the API locally and simulate AWS Lambda and DynamoDB on your local machine.

Contributing
------------

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for more information on making pull requests.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.
