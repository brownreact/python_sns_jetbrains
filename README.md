# Python SNS Message Tool

A very very basic tool that will send an SNS message to an AWS SNS topic defined by environment variables.

## Pre-requisites

An [AWS SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) Topic/Subscription has been set up, and the arn is available

## Environment Variables

- SNS_TOPIC
- SNS_MESSAGE
- AWS_REGION
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_SESSION_TOKEN

Where the AWS env vars are for the profile where the AWS SNS topic is housed, and the SNS_TOPIC is the arn of the SNS topic. Easiest way is to define these in a .env file. The message will be published depending on how the AWS SNS Topic/Subscription have been set up.
> NB The values of these variables should not be quoted in the env file.

## Building and Running the tool

### Build

```bash
cd build
./build-docker.sh <bitbucketuser> <bitbucketpass>
```

### Run

```bash
docker run --env-file <your_env_file>.env python_sns
```

## Expected output

```bash
+ python entry.py
{"uid": "985232f6-3130-4eb7-96d1-9dccfe45d1c6", "tool_version": "unknown", "timestamp": "2019-09-12 12:40:16.440", "tool": "sns_alert", "module": "log", "filename": "log.py", "levelno": 20, "lineno": 143, "correlation": "", "message": "Created Logger with name sns_alert", "funcName": "setup_log", "parent_uid": "8a198c71-f714-42f9-a8e8-2626d0fb4a50", "levelname": "INFO"}
{"uid": "985232f6-3130-4eb7-96d1-9dccfe45d1c6", "tool_version": "unknown", "timestamp": "2019-09-12 12:40:16.440", "tool": "sns_alert", "module": "core", "filename": "core.py", "levelno": 20, "lineno": 8, "correlation": "", "message": "Sending sns message", "funcName": "main", "parent_uid": "8a198c71-f714-42f9-a8e8-2626d0fb4a50", "levelname": "INFO"}
{"uid": "985232f6-3130-4eb7-96d1-9dccfe45d1c6", "tool_version": "unknown", "timestamp": "2019-09-12 12:40:22.778", "tool": "sns_alert", "module": "core", "filename": "core.py", "levelno": 20, "lineno": 10, "correlation": "", "message": "Sent sns message", "funcName": "main", "parent_uid": "8a198c71-f714-42f9-a8e8-2626d0fb4a50", "levelname": "INFO"}
```
