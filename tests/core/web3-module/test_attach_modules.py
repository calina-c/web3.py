from eth_utils import (
    is_integer,
)


def test_attach_modules(web3, module1, module2, module3, module4):
    web3.attach_modules({
        'module1': module1,
        'module2': (module2, {
            'submodule1': (module3, {
                'submodule2': module4,
            }),
        })
    })

    # assert module1 attached
    assert hasattr(web3, 'module1')
    assert web3.module1.a == 'a'
    assert web3.module1.b == 'b'

    # assert module2 + submodules attached
    assert hasattr(web3, 'module2')
    assert web3.module2.c == 'c'
    assert web3.module2.d() == 'd'

    assert hasattr(web3.module2, 'submodule1')
    assert web3.module2.submodule1.e == 'e'
    assert hasattr(web3.module2.submodule1, 'submodule2')
    assert web3.module2.submodule1.submodule2.f == 'f'

    # assert default modules intact
    assert hasattr(web3, 'geth')
    assert hasattr(web3, 'eth')
    assert is_integer(web3.eth.chain_id)


def test_attach_modules_that_do_not_inherit_from_module_class(
    web3, module1_unique, module2_unique, module3_unique, module4_unique,
):
    web3.attach_modules(
        {
            'module1': module1_unique,
            'module2': (module2_unique, {
                'submodule1': (module3_unique, {
                    'submodule2': module4_unique,
                }),
            })
        }
    )

    # assert module1 attached
    assert hasattr(web3, 'module1')
    assert web3.module1.a == 'a'

    # assert module2 + submodules attached
    assert hasattr(web3, 'module2')
    assert web3.module2.b == 'b'
    assert web3.module2.c() == 'c'

    assert hasattr(web3.module2, 'submodule1')
    assert web3.module2.submodule1.d == 'd'
    assert hasattr(web3.module2.submodule1, 'submodule2')
    assert web3.module2.submodule1.submodule2.e == 'e'

    # assert default modules intact
    assert hasattr(web3, 'geth')
    assert hasattr(web3, 'eth')
    assert is_integer(web3.eth.chain_id)
