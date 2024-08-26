import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { Field, Form, ErrorMessage, defineRule } from 'vee-validate'
import { required, email } from '@vee-validate/rules'
import { setLocale } from '@vee-validate/i18n'

// every request made with Axios includes the JWT token in the Authorization header.

import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken')
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

const app = createApp(App)

// vee-validate configuration

app.component('Form', Form)
app.component('Field', Field)
app.component('ErrorMessage', ErrorMessage)

// Set default locale
setLocale('en')

defineRule('required', required)
defineRule('email', email)

// Define the 'sameAs' rule for the register view
defineRule('sameAs', (value, [target]) => {
  if (value === target) {
    return true
  }
  return 'The passwords do not match'
})

app.use(router)

app.mount('#app')
