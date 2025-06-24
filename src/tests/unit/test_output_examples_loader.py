import pytest
import yaml
from src.infrastructure.loaders.output_example_yaml__loader import load_output_examples

def test_load_output_examples_success(tmp_path):
    content = {"a":"1","b":"2"}
    p = tmp_path/"out.yaml"
    p.write_text(yaml.dump(content))
    res = load_output_examples(str(p))
    assert res == content

def test_load_output_examples_not_found():
    with pytest.raises(FileNotFoundError):
        load_output_examples("no-such-file.yaml")