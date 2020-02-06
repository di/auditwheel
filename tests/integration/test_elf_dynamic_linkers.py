import platform
import pytest
from auditwheel.wheel_abi import analyze_wheel_abi


@pytest.mark.skipif(platform.machine() != 'ppc64le', reason='only supported on ppc64le')
def test_analyze_wheel_abi_elf_dynamic_linkers_ppc64le():
    winfo = analyze_wheel_abi(
        'tests/integration/numpy-1.18.1-cp36-cp36m-linux_ppc64le.whl')
    external_libs = winfo.external_refs['manylinux2014_ppc64le']['libs']
    assert len(external_libs) == 0

@pytest.mark.skipif(platform.machine() != 's390x', reason='only supported on s390x')
def test_analyze_wheel_abi_elf_dynamic_linkers_s390x():
    winfo = analyze_wheel_abi(
        'tests/integration/numpy-1.18.1-cp36-cp36m-linux_s390x.whl')
    external_libs = winfo.external_refs['manylinux2014_ppc64le']['libs']
    assert len(external_libs) == 0
