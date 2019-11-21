import datetime
import os
import subprocess

import pytest

@pytest.fixture
def tmp_file_root():
    return f'build/tmp{int(datetime.datetime.now().timestamp())}'

def run(cmd):
    subprocess.call(cmd, shell=True)

def test_wrapper_script_runs_blueprinta_in_docker(tmp_file_root):
    input_file = f'{tmp_file_root}.xlsx'
    output_file = f'{tmp_file_root}.svg'

    run(f'cp examples/blueprinta.xlsx {input_file}')
    run(f'./blueprinta {input_file} {output_file}')

    assert os.path.exists(output_file)