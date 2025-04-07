import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--testsuite", action="store", default="all"
    )

def pytest_collection_modifyitems(config, items):
    testsuite = config.getoption("--testsuite")
    if testsuite == "all":
        return
    selected_marker = testsuite
    skip_marker = pytest.mark.skip(reason=f"Skipping tests not in the {testsuite} suite")
    for item in items:
        if selected_marker not in item.keywords:
            item.add_marker(skip_marker)
