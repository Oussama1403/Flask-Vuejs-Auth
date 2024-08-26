<template>
  <div class="hello">
    <div>
      <div class="wrap">
        <h1>Welcome, {{ username }}</h1>
        <h2>
          <p>You have successfully logged in!<br /><br /></p>
        </h2>
        <button class="logout-button" @click="logout">Logout</button>
      </div>
    </div>
  </div>
</template>

<script>
import { jwtDecode } from 'jwt-decode'

export default {
  name: 'Hello',
  data() {
    return {
      username: ''
    }
  },
  mounted() {
    // Retrieve the username from local storage (authToken)
    const token = localStorage.getItem('authToken')
    const decoded = jwtDecode(token)
    const username = decoded.username
    this.username = username
  },
  methods: {
    logout() {
      localStorage.removeItem('authToken')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.hello {
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100%;
  text-align: center;
  margin: 0px;
  padding: 0px;
  color: #fff;
  font-family: 'Montserrat', sans-serif;
  background: linear-gradient(-145deg, #ee7752, #e73c7e, #23a6d5, #23d5ab, #d5c023, #ecece9);
  background-size: 400% 400%;
  -webkit-animation: Gradient 15s ease infinite;
  -moz-animation: Gradient 15s ease infinite;
  animation: Gradient 15s ease infinite;
}

.wrap h1 {
  font-size: 30px;
  font-weight: 700;
  margin: 1em;
}

.wrap h2 {
  font-size: 24px;
  font-weight: 400;
  line-height: 1.6;
  margin: 1em;
}
.logout-button {
  padding: 16px 32px;
  margin: 4px;
  border: 1px solid #ffffff;
  background: transparent;
  height: 50px;
  width: 100%;
  border-radius: 25px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 15px;
  line-height: 1.5;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 25px;
  transition: all 0.4s;
}

.logout-button:hover {
  cursor: pointer;
  background: #ffffff;
  color: #626262;
}

.logout-button:focus {
  background: #626262;
  border-color: #626262;
  box-shadow: none;
}

@-webkit-keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

@-moz-keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

@keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}
</style>
