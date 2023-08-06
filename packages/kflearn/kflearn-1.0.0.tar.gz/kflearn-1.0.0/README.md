## 确保已经安装setuptools 和 wheel

pip install --upgrade setuptools wheel twine

### 打包源码和编译

> python setup.py bdist_wheel  
> python setup.py sdist  
> python3 setup.py sdist bdist_wheel

* dist/ 目录中生成两个文件
    * example_pkg_your_username-0.0.1-py3-none-any.whl
    * example_pkg_your_username-0.0.1.tar.gz

### 检查并上传

python setup.py install # 安装  
twine check dist/*
twine upload dist/*
pip install -U example_pkg -i https://pypi.org/simple # 安装最新的版本测试