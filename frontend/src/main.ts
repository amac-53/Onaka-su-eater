import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Paginate from 'vuejs-paginate'


const app = createApp(App)
// app.config.errorHandler = () => null;
app.config.warnHandler = () => null;
app.use(router)
app.component('paginate', Paginate)
app.mount('#app')
