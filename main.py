def main():
    from multi_ver_lib.v1_0_0.feature import get_something as get_something_v1
    from multi_ver_lib.v2_0_0.feature import get_something as get_something_v2
    print(get_something_v1())
    print(get_something_v2())


if __name__ == "__main__":
    main()
