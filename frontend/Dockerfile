FROM node:16

WORKDIR /frontend

# vite/deps_tempへの実行権付与
CMD sh -c "chmod 777 /frontend/node_modules && npm install && npm run dev"
