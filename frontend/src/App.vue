<template>
  <div id="app">
    <form class="container" @submit.prevent="submit">
      <div class="row">
        <div class="col-sm-3">
          <h2 class="text-left mb-4"> Регистры: </h2>
          <div v-for="i in 13" :key="i" class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text" id="basic-addon2">R{{i}}</span>
            </div>
            <input type="number" v-model="registers[i - 1]" class="form-control" placeholder="Value" aria-label="" aria-describedby="basic-addon2">
          </div>
        </div>
        <div class="col-sm-4 ml-5 mr-5">
          <h2 class="text-left mb-4"> Команды: </h2>
          <div class="bg-danger text-left text-white mb-5 px-3 py-3" v-if="error">
            <h4> Ошибка! </h4>
            Code: {{ error.code }}
            <br>
            Response: {{ error.response }}
          </div>
          <div class="form-group text-left">
            <textarea required v-model="code" rows="10" class="form-control" id="exampleFormControlTextarea1"></textarea>
          </div>

          <div style="margin-left: 0; margin-right: 0" class="row justify-content-end">
            <button type="submit" class="btn btn-primary"><spinner v-if="loading" /> <template v-else>Загрузить на процессор</template></button>
          </div>
        </div>

        <div class="col-sm-3">
          <h2 class="text-left mb-4"><button @click="swapRegisters" v-if="hasResultRegisters" type="button" class="btn btn-primary mr-1"><i class="material-icons d-block">swap_horiz</i></button> Контекст:</h2>
          <div v-for="i in 13" :key="i" class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text" id="basic-addon2">R{{i}}</span>
            </div>
            <input disabled type="number" v-model="resultRegisters[i - 1]" class="form-control" placeholder="Value" aria-label="" aria-describedby="basic-addon2">
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import Spinner from '@/components/Spinner';
import axios from 'axios';

export default {
  name: 'app',
  components: {
    Spinner,
  },
  data() {
    return {
      registers: new Array(13).fill(0),
      resultRegisters: new Array(13),
      code: '',
      loading: false,
      error: null
    };
  },
  computed: {
    hasResultRegisters() {
      return this.resultRegisters.some(item => item != null);
    }
  },
  methods: {
    async submit() {
      this.loading = true;
      const { code, registers } = this;

      try {
        const res = await axios.post('/api', { code, registers });
        this.resultRegisters = res.data.registers;
        this.error = null;
      } catch(e) {
        this.error = { code: e.code, response: e.response };
      }

      this.loading = false
    },

    swapRegisters() {
      this.registers = [...this.resultRegisters];
      this.resultRegisters = new Array(13);
      
    }
    
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.form-control:disabled, .form-control[readonly] {
    background-color: #fff;
    opacity: 1;
}
</style>
