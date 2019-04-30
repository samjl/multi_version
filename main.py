import importlib


class Device(object):
    def __init__(self, version):
        mod = importlib.import_module(
            "multi_ver_lib.{}.feature".format(version)
        )
        print(mod)
        self.feature = mod.get_feature(version)


def main():
    v1_device = Device("v1_0_0")
    v2_device = Device("v2_0_0")

    v1_device.feature.set_id(3)
    print(v1_device.feature.get_id())
    print(v2_device.feature.get_id())

    v2_device.feature.set_id(2)
    print(v1_device.feature.get_id())
    print(v2_device.feature.get_id())


if __name__ == "__main__":
    main()
