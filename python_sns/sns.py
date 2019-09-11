import boto3
import logging
import python_sns.config as config

Logger = logging.getLogger(config.TOOLNAME)


def test_sns_message(configuration):
    session = boto3.Session(profile_name="naimuriplayground")
    client = session.client('sns', region_name='eu-west-1')
    try:
        client.publish(TopicArn=get_sns_alert_topic(configuration),
        Message=get_sns_alert_message(configuration)
        )
    except BaseException as err:
        Logger.error(str(err))
        raise err

def get_sns_alert_topic(configuration):
    return configuration.mappings[config.ENV_VAR_SNS_TOPIC]

def get_sns_alert_message(configuration):
    return configuration.mappings[config.ENV_VAR_SNS_MESSAGE]