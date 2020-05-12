import kvm_player

class TestKVMK8sBasic(kvm_player.KernelVirtualMachinePlayer):
    @classmethod
    def setUpClass(cls) -> None: ...

class TestKVMK8SBasic0(TestKVMK8sBasic):
    def test_00(self) -> None: ...

class TestKVMK8SBasic1(TestKVMK8sBasic):
    def test_01(self) -> None: ...
