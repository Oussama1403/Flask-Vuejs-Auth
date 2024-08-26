import { createRouter, createWebHistory } from 'vue-router'

import Login from '@/views/Auth/Login.vue'
import Signup from '@/views/Auth/Signup.vue'
import Hello from '@/views/Hello.vue'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/',
    name: 'Hello',
    component: Hello,
    meta: { requiresAuth: true } // Protected route
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// This beforeEach guard checks if the route the user is navigating to requires
// authentication. If it does, and the user is not authenticated (i.e. there is
// no authentication token stored in local storage), then the user is redirected
// to the login page. Otherwise, the user is allowed to continue on to their
// desired route.

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth)
  const isAuthenticated = !!localStorage.getItem('authToken')

  if (requiresAuth && !isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
