import python_sns.config as config
import python_sns.core as core
from cyrm_python_tools_framework.framework import post_parse_log, run_id
import sys
import logging

# Constructs the logger
post_parse_log(config.TOOLNAME, "", run_id(), run_id())

LOGGER = logging.getLogger(config.TOOLNAME)


def main():
    """
    Main entry point
    """
    configuration_set = config.Configuration()
    good, messages = configuration_set.valid()
    if not good:
        for msg in messages:
            LOGGER.error(msg)
    else:
        try:
            core.main(configuration_set)
        except BaseException as err:
            LOGGER.error(err)


if __name__ == "__main__":
    main()