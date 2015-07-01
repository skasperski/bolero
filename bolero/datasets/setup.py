def configuration(parent_package="", top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration("datasets", parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)
    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(**configuration(top_path="").todict())
