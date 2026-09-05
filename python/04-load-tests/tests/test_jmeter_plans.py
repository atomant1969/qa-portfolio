import xml.etree.ElementTree as ET
from pathlib import Path

import pytest


pytestmark = pytest.mark.load


@pytest.mark.parametrize("plan_name", ["jdbc-load-test-plan.jmx", "tcp-load-test-plan.jmx"])
def test_jmeter_plan_is_valid_xml(jmeter_dir, plan_name):
    plan_path = jmeter_dir / plan_name

    tree = ET.parse(plan_path)

    assert tree.getroot().tag == "jmeterTestPlan"


def test_jdbc_plan_targets_non_web_sampler(jmeter_dir):
    content = (jmeter_dir / "jdbc-load-test-plan.jmx").read_text(encoding="utf-8")

    assert "JDBCSampler" in content
    assert "HTTPSamplerProxy" not in content


def test_tcp_plan_targets_non_web_sampler(jmeter_dir):
    content = (jmeter_dir / "tcp-load-test-plan.jmx").read_text(encoding="utf-8")

    assert "TCPSampler" in content
    assert "HTTPSamplerProxy" not in content
