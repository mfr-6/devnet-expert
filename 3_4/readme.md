- Testbed: file that contains all device declaration along with connection type used and credentials

The device name in the testbed yaml file must match the configured hostname of the device. This is the #1 "gotcha"s with connecting to a device. Alternatively you can use the learn hostname feature which will learn the hostname during the initial connection.

```
"There's two kinds of people using PyATS. Those who have been bit by the case sensitive hostname issue, and those who WILL get bit by the case sensitive hostname issue." - Jeremy Bresley
```

### Supported platforms
https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/supported_platforms.html

### Supported apis/services
https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/services/index.html

### Supported models (like interface, ospf, etc)
https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models



### Mock devices setup

Mock device - python script that mimics the real devices

```
mock_device_cli --os nxos \
                --mock_data_dir mock_devices/working/nxos \
                --state execute
```

### PyATS commands

- learn: takes the snapshot of network using testbed file and specific model
```
pyats learn interface ospf platform --testbed-file <filename> --output <filename>
```
- diff: compare two snapshots - to preview - open file in output snapshot directory
```
pyats diff <snap1> <snap2> --output <another_snap>
```
- To take snapshot of the show command, use `pyats parse`
```
pyats parse "<command>" --testbed-file <file> --output <shapshot name> --device <device_name_from_testbed>
```
- pyats parse snapshots can be compared
```
pyats diff <snapshot_a> <snapshot_b> --output <diff snapshot>
```

### PYTHON

To load testbed, use `load` method

```
from genie.testbed import load
testbed = load('filename')
```

To connect to device, get device from testbed

```
device = testbed.devices['device-name`]
device.connect()
```

To execute commands, use `execute` method in a device level

```
output = device.execute("show version")
```

To get parsed output, use `parse`

```
parsed = device.parse("show version")
```

To configure device, use `configure`. This API will enter `configure terminal`, enter config, then it will exit using `config terminal` back to `enable mode`. If any configuration is invalid, exception will be raised

```
configuration = '''\
interface ethernet2/1
shutdown'''
OR

configuration = [
    'interface ethernet2/1',
    'shutdown'
]

output = device.configure(configuration)
```

Learn API is a `pyats learn` equivalent in Python
```
output = device.learn("interface")
print(output.info)
```




`genie parse --help`