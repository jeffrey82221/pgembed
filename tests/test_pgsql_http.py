import sys

import pgembed_pgsql_http


def test_get_extension_path_uses_platform_library_name(tmp_path, monkeypatch):
    package_dir = tmp_path / "pgembed_pgsql_http"
    package_dir.mkdir()
    extension_path = package_dir / pgembed_pgsql_http.EXTENSION_SO
    extension_path.touch()
    monkeypatch.setattr(
        pgembed_pgsql_http, "__file__", str(package_dir / "__init__.py")
    )

    expected_name = "http.dylib" if sys.platform == "darwin" else "http.so"
    assert pgembed_pgsql_http.EXTENSION_SO == expected_name
    assert pgembed_pgsql_http.get_extension_path() == extension_path
