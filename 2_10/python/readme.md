## NSO Maagic Python API

### Flow of using API

1. Create a transaction
2. Access device information
3. Manipulate data
4. Apply configurations
5. Close the transaction

### Transaction types

There are several options for opening connection to NSO through the API.

- `single_read_trans`
- `single_write_trans`

### Transaction example 

`with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:`

This statement opens read-write transaction to NSO - similar to entering config mode on CLI. 
    
NSO Maagic API docs: https://developer.cisco.com/docs/nso/api/#!ncs




### Other 

Output from NCS CLI when executing configuration through Python Maagic API
```
admin@ncs# 
System message at 2024-02-15 05:22:07...
Commit performed by admin via tcp using python.
```

If device is out-of-sync - it's not possible to configure new items

```
(main) expert@expert-cws:~/src/tasks/devnet-expert/2_10/python$ python ncs_conf.py 
Traceback (most recent call last):
  File "/home/expert/src/tasks/devnet-expert/2_10/python/ncs_conf.py", line 12, in <module>
    t.apply()
  File "/home/expert/venvs/main/lib/python3.9/site-packages/ncs/maapi.py", line 2126, in apply
    self.maapi.apply_trans_flags(self.th, keep_open, flags)
  File "/home/expert/venvs/main/lib/python3.9/site-packages/ncs/maapi.py", line 423, in proxy
    return real(self2.msock, *args, **kwargs)
_ncs.error.Error: Unknown error (65): Network Element Driver: device dist-rtr01: out of sync
```

NSO CLI Output:
```
admin@ncs# *** ALARM connection-failure: Failed to connect to device dist-rtr01: connection refused: NEDCOM CONNECT: Connect timed out in new state
admin@ncs# *** ALARM out-of-sync: Device dist-rtr01 is out of sync
```