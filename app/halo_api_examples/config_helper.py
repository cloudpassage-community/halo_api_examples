import os
import sys


class ConfigHelper():
    """
        Manage all configuration information for the application
    """
    def __init__(self):
        ERROR = 1
        NEWLINE = "\n"
        EMPTY = ""

        self.halo_key = os.getenv("HALO_API_KEY")
        self.halo_secret = os.getenv("HALO_API_SECRET_KEY")

        # server groups used in examples
        server_group = ""
        server_group_temp = ""
        server_ip = ""
        error_string = ""

        server_group = os.environ["SERVER_GROUP"] = "<server_group>"
        server_group_temp = \
            os.environ["SERVER_GROUP_TEMP"] = "<server_group_temp>"
        server_ip = os.environ["SERVER_IP"] = "<server_ip>"

        # check configuration
        if server_group == EMPTY:
            error_string = "Environment variable SERVER_GROUP is empty"
        elif server_group_temp == EMPTY:
            error_string = "Environment variable SERVER_GROUP_TEMP is empty"
        elif server_ip == EMPTY:
            error_string = "Environment variable SERVER_IP is empty"

        if server_group == EMPTY or server_group_temp == EMPTY \
                or server_ip == EMPTY:
            print "Invalid configuration: %s... Exiting...%s" % (error_string,
                                                                 NEWLINE)
            sys.exit(ERROR)
