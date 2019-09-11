import python_sns.sns as sns_message
import python_sns.config as config
import logging

Logger = logging.getLogger(config.TOOLNAME)

def main(configuration):
    Logger.info("Sending sns message")
    sns_message.test_sns_message(configuration)
    Logger.info("Sent sns message")