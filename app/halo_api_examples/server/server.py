import os


class Server(object):
    """
       This class will work with Halo server groups.
    """

    ##########
    #
    #   Halo Server examples
    #
    #   Parameters:
    #
    #       self (object) - A Server object
    #       halo (object) - A HaloGeneral object
    #
    ##########

    def __init__(self, halo):
        # the HaloGeneral instance for API calls
        self.server_fqdn = None
        self.server_group_name = None
        self.server_id = None
        self.server_group_id = None

        self.halo = halo
        # a Halo Server Group object
        self.halo_server_object = halo.get_server_obj()

    def run_server_examples(self):
        NEWLINE = "\n"

        servers = self.list_all_servers()
        self.server_in_group(servers)

        print "%sThe Halo server we will play with in our examples is " \
              "in the group \"%s\" with an FQDN of %s.%s" \
              % (NEWLINE, self.server_group_name, self.server_fqdn,
                 NEWLINE)

        self.move_server_to_temp_group()
        self.move_server_to_example_group()

    ###
    #
    #   get all servers
    #
    #   Parameters:
    #       self (object) - Server object
    #
    #   Return:
    #       servers (list) - list of servers
    #
    ###
    def list_all_servers(self):
        NEWLINE = "\n"

        servers = \
            self.halo.list_all_servers(self.halo_server_object)

        ###
        #
        #   Print the servers
        #
        ###
        print "%sThe servers in the account are:%s%s" % (NEWLINE, servers,
                                                         NEWLINE)

        return servers

    ###
    #
    #   See if we have a server to work with in our API example group
    #
    #   Parameters -
    #       self (object) - Server object
    #       servers (list) - list of servers
    #
    #   Return -
    #       server_in_api_example_group (bool) - bool telling if we have one
    #
    ###
    def server_in_group(self, servers):
        ID = "id"
        FQDN = "connecting_ip_fqdn"
        SERVER_GROUP_ID = "group_id"
        SERVER_GROUP = "group_name"

        self.server_group_name = os.getenv("SERVER_GROUP")

        # nothing to do if we don't have a server to use
        server_in_api_example_group = False

        for server in servers:
            if server[SERVER_GROUP] == self.server_group_name:
                # get info about the server we want to play with
                server_in_api_example_group = True
                print "%s" % (server[FQDN])
                self.server_fqdn = server[FQDN]
                self.server_id = server[ID]
                self.server_group_id = server[SERVER_GROUP_ID]
            else:
                print "%s" % (server[FQDN])

        return server_in_api_example_group

    ###
    #
    #   Moves server to a temporary group
    #
    #   Parameters:
    #
    #       self (object) - Server object
    #
    #   Return:
    #
    #       ret_val (bool) - True or False from assign call
    #
    ###
    def move_server_to_temp_group(self):
        NEWLINE = "\n"
        ret_val = None

        SERVER_GROUP = "group_name"

        halo_server_group_obj = self.halo.get_server_group_obj()

        # get temp server group ID
        server_group_temp_name = os.getenv("SERVER_GROUP_TEMP")

        server_group_temp_id = \
            self.halo.get_server_group_id_by_name(halo_server_group_obj,
                                                  server_group_temp_name)

        # assign to temp group
        ret_val = self.halo.assign_server_to_group(self.halo_server_object,
                                                   self.server_id,
                                                   server_group_temp_id)

        # describe server
        description = self.halo.describe_server(self.halo_server_object,
                                                self.server_id)

        print "The Halo server with an FQDN of %s is now in the " \
              "\"%s\" group.%s" \
              % (self.server_fqdn, description[SERVER_GROUP], NEWLINE)

        return ret_val

    ###
    #
    #   Moves server to the example group
    #
    #   Parameters:
    #
    #       self (object) - Server object
    #
    #   Return:
    #
    #       ret_val (bool) - True or False from assign call
    #
    ###
    def move_server_to_example_group(self):
        SERVER_GROUP = "group_name"
        NEWLINE = "\n"
        ret_val = None

        # move server to example group
        ret_val = self.halo.assign_server_to_group(self.halo_server_object,
                                                   self.server_id,
                                                   self.server_group_id)

        # describe server
        description = self.halo.describe_server(self.halo_server_object,
                                                self.server_id)

        print "The Halo server with an FQDN of %s is now in the " \
              "\"%s\" group.%s" \
              % (self.server_fqdn, description[SERVER_GROUP], NEWLINE)

        return ret_val
