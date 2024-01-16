import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./front_src', import.meta.url))
    }
  },
  server: {
    port: process.env.PORT || 5000,
  },
  build:{
    outDir: './dist'
  },

})
