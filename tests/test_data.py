from src.config import PROJ_ROOT, RAW_DATA_DIR


def test_project_root_exists():
    assert PROJ_ROOT.exists()


def test_raw_data_dir_is_inside_project():
    assert RAW_DATA_DIR.is_relative_to(PROJ_ROOT)