<template>
  <div class="v-main">
      Главная страница
      <div class="games_list">

      </div>
  </div>
</template>

<script>
export default {
    name: 'Main',
    data(){

    },
    created(){
        this.getGameList()
    },
    methods:{
        getGameList(){
            
        }
    }
}
</script>

<style>

</style>