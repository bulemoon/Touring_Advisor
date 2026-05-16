export {}

declare global {
  interface Window {
    CONFIG: {
      API_BASE_URL: string
      AMAP_JS_KEY: string
    }
  }
}
