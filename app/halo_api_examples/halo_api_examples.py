import os
from server_group.server_group import ServerGroup
from server.server import Server


class HaloApiExamples(object):
    """
       This class will enable LIDS to monitor a directory
       rather than a target file.
    """
    def __init__(self, halo):

        self.halo = halo

        server_group_obj = ServerGroup(halo)
        self.halo_server_group_examples(server_group_obj)

        server_obj = Server(halo)
        self.halo_server_examples(server_obj)

        self.clean_up()

    @classmethod
    def halo_server_group_examples(self, server_group_obj):
        server_group_obj.run_server_group_examples()

    @classmethod
    def halo_server_examples(self, server_obj):
        server_obj.run_server_examples()

    def clean_up(self):
        # remove server groups
        halo_server_group_obj = self.halo.get_server_group_obj()

        server_group_name = os.getenv("SERVER_GROUP")
        server_group_id = \
            self.halo.get_server_group_id_by_name(halo_server_group_obj,
                                                  server_group_name)
        force = True
        self.halo.delete_server_group(halo_server_group_obj,
                                      server_group_id, force)

        server_group_name = os.getenv("SERVER_GROUP_TEMP")
        server_group_id = \
            self.halo.get_server_group_id_by_name(halo_server_group_obj,
                                                  server_group_name)
        self.halo.delete_server_group(halo_server_group_obj,
                                      server_group_id)
