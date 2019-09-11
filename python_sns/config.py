import os

TOOLNAME = "sns_alert"
ENV_VAR_SNS_TOPIC = "SNS_TOPIC"
ENV_VAR_SNS_MESSAGE = "SNS_MESSAGE"

class Configuration(object):
    def __init__(self):
        self.mappings = {
            ENV_VAR_SNS_TOPIC: None,
            ENV_VAR_SNS_MESSAGE: None
        }
        for key in self.mappings:
            self.mappings[key] = os.environ.get(key)

    def valid(self):
        v = True
        messages = []
        for key, value in self.mappings.iteritems():
            if value is None or value == "":
                v = False
                messages.append("Missing env var %s" % (key))
        return (v, messages)

    

