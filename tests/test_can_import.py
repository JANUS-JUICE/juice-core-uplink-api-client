def test_import_package():
    """Verify we can import the main package"""
    import juice_core_uplink_api_client

def test_has_version():
    """Check that the package has an accesible __version__"""
    import juice_core
    version = juice_core.__version__