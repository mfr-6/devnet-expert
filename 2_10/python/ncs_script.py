import ncs

with ncs.maapi.single_read_trans("admin", "admin", groups=["ncsadmin"]) as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device["dist-rtr01"]
    cdp_result = device.config.ios__cdp.run
    print(
        "For Device {}, CDP being enabled is {}".format(device.name, cdp_result)
    )
