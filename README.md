The project shows API examples using the Halo Python SDK

API Setup
---------

A) Install the CloudPassage SDK
1) Type: pip install cloudpassage

2) Configure the SDK
1) Type: sudo vi /etc/cloudpassage.yaml

defaults:  
  key_id: <key>  
  secret_key: <secret>  
  api_hostname: api.cloudpassage.com  
  api_port: 443  

or

export HALO_API_KEY=<key>  
export HALO_API_SECRET_KEY=<secret>  
export HALO_API_HOSTNAME=api.cloudpassage.com

Project Configuration
---------------------

app/halo_api_examples/config_helper.py stores the configuration for the project.

The project will use two servers groups for the examples.  A primary and secondary.

1) Enter the name of the primary server group and enter it as the value for os.environ["SERVER_GROUP"]
2) Enter the name of the secondary server group and enter it as the value for os.environ["SERVER_GROUP_TEMP"].
3) Enter the public IP of the server that will be used for the examples in os.environ["SERVER_IP"].  This server
needs to have the Halo agent running on it.

HaloGeneral
-----------

HaloGeneral is a class that wraps API functionality.  The HaloGeneral project will need to be in the root of this
project.  To obtain it, in the project root directory execute the following command:
git clone https://github.com/jgibbons-cp/halo_general.git

Project Execution
-----------------

In the project root type the following command: python app/runner.py

Project Classes
---------------

1) ConfigHelper - location: app/halo_api_examples/config_helper.py

This is the project configuration as noted above in section "Project Configuration"

2) ServerGroup - location: app/halo_api_examples/server_group/server_group.py

This includes Halo ServerGroup examples.

A) Create the primary Halo server group and output server group name and ID  
B) Get the server ID  
C) Move the host we will use for the examples to the primary server group  
D) Create the secondary Halo server group and output server group name and ID  
E) Call list all server groups and print details of the first one  
F) Get the first server group details and output active, deactivated, missing and total servers in the group  
G) Get all servers in a group and list active servers by FQDN

3) Server - location: app/halo_api_examples/server_group/server.py

This includes Halo ServerGroup examples.

A) Get all servers in the account and print them out by FQDN  
B) Print the server we will use in the examples (the server in the primary server group)  
C) Move the server to the secondary group using describe server  
D) Move the server back to the primary group using describe server  

4) HaloApiExamples - location: app/halo_api_examples/halo_api_examples.py

This class executes the examples in the API example classes.

Tests
-----

1) Unit

A) ConfigHelper - location: halo_api_examples/app/test/unit/test_config_helper.py

Unit tests for config_helper.py.  Must have a configuration to run.

B) ServerGroup - location: halo_api_examples/app/test/unit/test_server_group_methods.py

Unit tests for server_group.py.  Must have a configuration to run.

C) Server - location: halo_api_examples/app/test/unit/test_server_methods.py

Unit tests for server.py.  Must not have a configuration to pass.

2) Style

A) pep8 checking - localtion: location: halo_api_examples/app/test/style/test_style_flake8.py

Checks code for pep8 issues