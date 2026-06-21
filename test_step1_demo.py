"""
==========================================
实验步骤 1 单元测试
==========================================
测试内容:
1. 首页返回 200 状态码
2. 页面包含 CI/CD 关键字
3. 页面包含学号 2440666125 和姓名 Laishisheng
4. /health 接口正常工作
"""
import pytest
from step1_demo import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    print("[测试 1] 首页返回 200 状态码...", end=" ")
    rv = client.get("/")
    assert rv.status_code == 200
    print("✅ 通过")


def test_index_contains_ci_cd_keyword(client):
    print("[测试 2] 页面包含 CI/CD 关键字...", end=" ")
    rv = client.get("/")
    assert b"CI/CD" in rv.data
    print("✅ 通过")


def test_index_contains_student_info(client):
    print("[测试 3] 页面包含学号和姓名...", end=" ")
    rv = client.get("/")
    data = rv.data.decode("utf-8")
    assert "2440666125" in data
    assert "赖石生" in data
    print("✅ 通过")


def test_health_check_endpoint(client):
    print("[测试 4] /health 接口正常工作...", end=" ")
    rv = client.get("/health")
    assert rv.status_code == 200
    assert rv.get_json()["status"] == "healthy"
    print("✅ 通过")


if __name__ == "__main__":
    print("=" * 60)
    print("  实验步骤 1 - 单元测试")
    print("=" * 60)
    pytest.main([__file__, "-v"])
