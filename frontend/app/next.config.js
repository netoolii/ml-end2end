require('path')

/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  sassOptions: {
    // includePaths: [path.join(__dirname, 'styles')]
  },
  env:{
    BACKEND_HOST: process.env.BACKEND_HOST,
    BACKEND_PORT: process.env.BACKEND_PORT,
    BACKEND_PATH_AUTH_LOGIN: process.env.BACKEND_PATH_AUTH_LOGIN,
    BACKEND_PATH_AUTH_LOGOUT: process.env.BACKEND_PATH_AUTH_LOGOUT,
    BACKEND_PATH_USER_LIST_CONVERSATION: process.env.BACKEND_PATH_USER_LIST_CONVERSATION,
    BACKEND_PATH_CONVERSATION_CREATE: process.env.BACKEND_PATH_CONVERSATION_CREATE,
    BACKEND_PATH_CONVERSATION_DELETE: process.env.BACKEND_PATH_CONVERSATION_DELETE,
    BACKEND_PATH_CONVERSATION_GET: process.env.BACKEND_PATH_CONVERSATION_GET,
    BACKEND_PATH_CONVERSATION_GET_LIST: process.env.BACKEND_PATH_CONVERSATION_GET_LIST,
    BACKEND_PATH_POST_GET: process.env.BACKEND_PATH_POST_GET,
    BACKEND_PATH_POST_CREATE: process.env.BACKEND_PATH_POST_CREATE
  },
  reactStrictMode: false,
  async redirects() {
    return [
      {
        source: '/',
        destination: '/chat',
        permanent: true
      }
    ]
  },
  logging: {
    fetches: {
      fullUrl: true
    }
  }
}

module.exports = nextConfig
