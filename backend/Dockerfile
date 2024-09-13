# 使用官方 Python 3.9 镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 将当前目录的内容复制到 Docker 容器中
COPY . .

# 安装 Python 依赖
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 运行 Django 服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
