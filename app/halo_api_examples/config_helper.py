import os
import sys


class ConfigHelper():
    """
        Manage all configuration information for the application
    """
    def __init__(self):
        ERROR = 1
        NEWLINE = "\n"

        self.halo_key = os.getenv("HALO_API_KEY")
        self.halo_secret = os.getenv("HALO_API_SECRET_KEY")

        # server groups used in examples
        error_string = ""

        server_group = os.environ["SERVER_GROUP"] = "<server_group>"

        server_group_temp = \
            os.environ["SERVER_GROUP_TEMP"] = "<server_group_temp>"
        server_ip = os.environ["SERVER_IP"] = "<server_ip>"

        # sed replaces teh defaults above once starting at line one
        # thus declaration here so no dependencies on line numbers
        SERVER_GROUP_DEFAULT = "<server_group>"
        SERVER_GROUP_TEMP_DEFAULT = "<server_group_temp>"
        SERVER_IP_DEFAULT = "<server_ip>"

        # check configuration
        if server_group == SERVER_GROUP_DEFAULT:
            error_string = "Environment variable SERVER_GROUP is empty"
        elif server_group_temp == SERVER_GROUP_TEMP_DEFAULT:
            error_string = "Environment variable SERVER_GROUP_TEMP is empty"
        elif server_ip == SERVER_IP_DEFAULT:
            error_string = "Environment variable SERVER_IP is empty"

        if server_group == SERVER_GROUP_DEFAULT or \
                server_group_temp == SERVER_GROUP_TEMP_DEFAULT \
                or server_ip == SERVER_IP_DEFAULT:
            print "Invalid configuration: %s... Exiting...%s" % (error_string,
                                                                 NEWLINE)
            sys.exit(ERROR)
