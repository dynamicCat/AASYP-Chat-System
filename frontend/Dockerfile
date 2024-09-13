# 使用Node.js官方镜像
FROM node:14

# 设置工作目录
WORKDIR /app

# 复制package.json和package-lock.json
COPY package*.json ./

# 安装依赖
RUN npm install

# 复制项目文件
COPY . .

# 构建React应用
RUN npm run build

# 启动React开发服务器
CMD ["npm", "start"]
