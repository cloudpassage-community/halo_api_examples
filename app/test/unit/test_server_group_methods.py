import imp
import os
import sys
import unittest

# import modules
here_dir = os.path.dirname(os.path.abspath(__file__))

module_name = 'config_helper'
module_path = os.path.join(here_dir, '../../halo_api_examples')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
config = imp.load_module(module_name, fp, pathname, description)

module_name = 'halo_general'
module_path = os.path.join(here_dir, '../../../halo_general')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
halo_general = imp.load_module(module_name, fp, pathname, description)

module_name = 'server_group'
module_path = os.path.join(here_dir, '../../halo_api_examples/server_group')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
server_group = imp.load_module(module_name, fp, pathname, description)


class TestServerGroupMethods(unittest.TestCase):
    '''
        Test the ServerGroup methods
    '''
    halo_config = config.ConfigHelper()
    halo = halo_general.HaloGeneral(halo_config)
    server_group_obj = server_group.ServerGroup(halo)

    def setUp(self):
        pass

    def test_server_group_create(self):
        '''
            Creating a server group should return a unicode string
            or get a validation exception string
        '''

        exception_string = "CloudPassageValidationException"

        server_group_name = "halo api example unit test group"
        server_group_id = \
            self.server_group_obj.create_server_group(server_group_name)

        if isinstance(server_group_id, str):
            self.assertEqual(server_group_id, exception_string)
        else:
            self.assertEqual(isinstance(server_group_id, unicode), True)

        halo_server_group_obj = self.halo.get_server_group_obj()
        force = True
        self.halo.delete_server_group(halo_server_group_obj, server_group_id,
                                      force)

    def test_list_all_server_groups(self):
        '''
            List all server groups
            Test to ensure a list is returned
        '''

        server_groups = self.server_group_obj.list_all_server_groups()
        self.assertEqual(isinstance(server_groups, list), True)

    def test_get_server_group_details(self):
        '''
            List all server groups
            Test to ensure a dict is returned
        '''
        server_groups = self.server_group_obj.list_all_server_groups()
        server_group_details = \
            self.server_group_obj.get_server_group_details(server_groups)
        self.assertEqual(isinstance(server_group_details, dict), True)

    def test_list_all_servers_in_group(self):
        '''
            Get all servers in a group
            Test to ensure a list is returned
        '''
        server_groups = self.server_group_obj.list_all_server_groups()
        server_group_details = \
            self.server_group_obj.get_server_group_details(server_groups)
        servers_in_group = \
            self.server_group_obj.list_all_servers_in_group(
                server_groups,
                server_group_details)

        self.assertEqual(isinstance(servers_in_group, list), True)


if __name__ == '__main__':
    unittest.main()
