import os
import sys


class ServerGroup(object):
    """
       This class will work with Halo server groups.
    """

    ##########
    #
    #   Halo Server Group examples
    #
    #   Parameters:
    #
    #       self (object) - A ServerGroup object
    #       halo (object) - A HaloGeneral object
    #
    ##########

    def __init__(self, halo):
        # the HaloGeneral instance for API calls
        self.halo = halo

        # a Halo Server Group object
        self.halo_server_group_object = halo.get_server_group_obj()

    ##
    #
    #   Execute examples of Server Group API functionality
    #
    ##

    def run_server_group_examples(self):
        ERROR = 1
        NEWLINE = "\n"

        # create server group for API examples
        halo_api_server_group = os.getenv("SERVER_GROUP")
        halo_api_example_group_id = \
            self.create_server_group(halo_api_server_group)

        # get server ID
        server_ip = os.getenv("SERVER_IP")
        halo_http_helper_obj = self.halo.get_http_helper_obj()
        server_id = self.halo.get_server_id_for_ip(halo_http_helper_obj,
                                                   server_ip)

        # make sure we have a server to work with
        if server_id is None:
            print "%sCan't continue without a server in \"%s\"... Does host" \
                    " with IP %s exist and have the Halo agent installed" \
                    " and started? Exiting..." \
                    "%s" % (NEWLINE, halo_api_server_group, server_ip, NEWLINE)

            force = True
            self.halo.delete_server_group(self.halo_server_group_object,
                                          halo_api_example_group_id, force)
            sys.exit(ERROR)

        # move server to Halo API Example group
        halo_server_obj = self.halo.get_server_obj()
        self.halo.assign_server_to_group(
            halo_server_obj, server_id,
            halo_api_example_group_id)

        # create secondary server group for API examples
        halo_api_server_group = os.getenv("SERVER_GROUP_TEMP")
        self.create_server_group(halo_api_server_group)

        # list all and print out info of first one
        server_groups = self.list_all_server_groups()

        # get detail of server group and print out some for user
        server_group_detail = self.get_server_group_details(server_groups)

        # get all servers and print out active ones
        self.list_all_servers_in_group(server_groups, server_group_detail)

    ###
    #
    #    create a server group
    #
    ###
    def create_server_group(self, server_group_name):
        NEWLINE = '\n'

        server_group_id = \
            self.halo.create_server_group(self.halo_server_group_object,
                                          server_group_name)

        print "%sHalo Server Group %s created with ID %s%s" \
              % (NEWLINE, server_group_name, server_group_id, NEWLINE)

        return server_group_id

    ###
    #
    #   list all server groups and print the name and ID of
    #   the first in the group
    #
    ###
    def list_all_server_groups(self):
        FIRST = 0
        ID = "id"
        NAME = "name"
        NEWLINE = "\n"

        server_groups = \
            self.halo.list_all_server_groups(self.halo_server_group_object)

        print "The first server group in the list is %s with the ID %s.%s" \
              % (server_groups[FIRST][NAME], server_groups[FIRST][ID],
                 NEWLINE)

        return server_groups

    ###
    #
    #   Get server group details
    #
    ###
    def get_server_group_details(self, server_groups):
        FIRST = 0
        ID = "id"
        NAME = "name"
        NEWLINE = "\n"
        WORKLOADS = "server_counts"
        ACTIVE_STATUS = "active"
        DEACTIVATED_STATUS = "deactivated"
        MISSING_STATUS = "missing"
        TOTAL = "total"

        server_group_id = server_groups[FIRST][ID]
        server_group_detail = \
            self.halo.describe_halo_server_group(
                self.halo_server_group_object, server_group_id)

        print "Further Server Group Details (not exhaustive) %s" % (NEWLINE)
        print "Active servers in %s: %s%s" \
              % (server_group_detail[NAME],
                 server_group_detail[WORKLOADS][ACTIVE_STATUS], NEWLINE)

        print "Deactived servers in %s: %s%s" \
              % (server_group_detail[NAME],
                 server_group_detail[WORKLOADS][DEACTIVATED_STATUS], NEWLINE)

        print "Missing servers in %s: %s%s" \
              % (server_group_detail[NAME],
                 server_group_detail[WORKLOADS][MISSING_STATUS], NEWLINE)

        print "Total servers in %s: %s%s" \
              % (server_group_detail[NAME],
                 server_group_detail[WORKLOADS][TOTAL], NEWLINE)

        return server_group_detail

    ###
    #
    #   get all servers in a group and list active servers by FQDN
    #
    ###
    def list_all_servers_in_group(self, server_groups, server_group_detail):
        NAME = "name"
        NEWLINE = "\n"
        ACTIVE_STATUS = "active"
        STATE = "state"
        FQDN = "connecting_ip_fqdn"
        FIRST = 0
        ID = "id"
        server_group_id = server_groups[FIRST][ID]

        servers_in_group = \
            self.halo.list_all_servers_in_group(self.halo_server_group_object,
                                                server_group_id)

        print "The active servers in %s are:%s" % (server_group_detail[NAME],
                                                   NEWLINE)

        for server in servers_in_group:
            if server[STATE] == ACTIVE_STATUS:
                print server[FQDN]

        return servers_in_group
