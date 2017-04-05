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

module_name = 'server'
module_path = os.path.join(here_dir, '../../halo_api_examples/server')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
server = imp.load_module(module_name, fp, pathname, description)


class TestServerGroupMethods(unittest.TestCase):
    '''
        Test the Server methods
    '''
    halo_config = config.ConfigHelper()
    halo = halo_general.HaloGeneral(halo_config)
    server_obj = server.Server(halo)

    def setUp(self):
        pass

    def test_list_all_servers(self):
        '''
            List all servers
            Test if return value is a list
        '''

        servers = self.server_obj.list_all_servers()

        self.assertEqual(isinstance(servers, list), True)

    def test_move_server_to_temp_group(self):
        '''
            Move server to temp group
            Test based on return call
        '''
        servers = self.server_obj.list_all_servers()
        ret_val = self.server_obj.server_in_group(servers)

        if ret_val is True:
            ret_val = self.server_obj.move_server_to_temp_group()
            self.assertEqual(ret_val, True)
        else:
            self.assertEqual(ret_val, False)

    def test_move_server_to_example_group(self):
        '''
            Move server to example group
            Test based on return call
        '''
        servers = self.server_obj.list_all_servers()
        ret_val = self.server_obj.server_in_group(servers)

        if ret_val is True:
            ret_val = self.server_obj.move_server_to_example_group()
            self.assertEqual(ret_val, True)
        else:
            self.assertEqual(ret_val, False)


if __name__ == '__main__':
    unittest.main()
