# SHT Rest Interface

This repository contains two modules to interact with the Juice Core Uplink 
API, both contained in the juice-core-uplink-api-client folder.

## juice-core-uplink-api-client
This module is automatically generated using the command below. It must not be 
modified manually.

```bash 
 openapi-python-client update --path openapi.json 
```

or just using the makefile `make` shortcut. The command is expected to be runt 
from the root of the repository (where the makefile is located) and requires 
`openapi-python-client` to be installed in the host system.

The module is generated from the openapi definition available at 
https://juicesoc.esac.esa.int/docs/, but **notice** that the openapi.json definition is a modified version of the one 
available at that link. The file was modified by:
- updating the file to openapi 3.0
- making several changes to fix inconsistencies in the definition

Also note that only some issues were corrected in the openapi.json file,
hence the generated module is not complete, and it is not granted to work.
If you find any additional inconsistency, please report it to the repo issue 
tracker.


## juice_core 
this module is a wrapper around the automatically generated module. It is made 
by a class with several methods to interact with the API. It is just a stub to 
start disucssing the API interface. It is not complete and it is not guaranteed 
to work.

## Usage example

First, create a client:

```python
from juice_core import SHTRestInterface
i = SHTRestInterface()
```
and access the list of available plans on the server:

```python
i.plans_dt
```

will output a pandas dataframe with the list of plans (just some here):

|    | trajectory   | name                       | mnemonic                   | is_public   | created                    |   id | author   | description                                                                                                                                                           | refine_log   | ptr_file                                                                |
|---:|:-------------|:---------------------------|:---------------------------|:------------|:---------------------------|-----:|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:------------------------------------------------------------------------|
|  0 | CREMA_3_0    | CASE4                      | CASE4                      | True        | 2021-03-04 13:29:58.835199 |   17 | rlorente | Demonstration Case 4                                                                                                                                                  |              |                                                                         |
|  1 | CREMA_5_0    | CREMA_5_0_OPPORTUNITIES_v0 | CREMA_5_0_OPPORTUNITIES_v0 | True        | 2021-08-26 09:12:06.767139 |   31 | cvallat  | 1st run opf opportunities generation (UC22), based on existing definitions of oppportunities (inherited from crema 3_0)                                               |              | https://juicesoc.esac.esa.int/rest_api/file/trajectory%23CREMA_5_0.ptx/ |
|  2 | CREMA_5_0    | CREMA_5_0_OPPORTUNITIES_v1 | CREMA_5_0_OPPORTUNITIES_v1 | True        | 2021-10-04 13:49:49.262682 |   36 | cvallat  | Added two opportunities for JMAG_CALROL for the last 2 perijoves before JOI (PJ69 not considered since too clsoe to GoI for observations to take place --> MPAD rule) |              | https://juicesoc.esac.esa.int/rest_api/file/trajectory%23CREMA_5_0.ptx/ |
|  3 | CREMA_5_0    | CREMA_5_0_OPPORTUNITIES_v2 | CREMA_5_0_OPPORTUNITIES_v2 | True        | 2021-10-05 07:24:07.742653 |   37 | cvallat  | Modified GANYMEDE_GM opportunity around 3G3 for WG3 prime allocation (1 hour centered at CA)                                                                          |              | https://juicesoc.esac.esa.int/rest_api/file/trajectory%23CREMA_5_0.ptx/ |


You can also directly interact with the underalying `juice-core-uplink-api-client` module:

```python
from juice_core_uplink_api_client.api.rest_api import rest_api_plan_list
from juice_core_uplink_api_client import Client
c = Client("https://juicesoc.esac.esa.int")
rest_api_plan_list.sync(client=c)
```