<template>
  <div class="v-main">
      <div class="userMain">
      <p>Вы вошли как {{username}}</p>
      <router-link to="/logout">Logout</router-link>
    </div>
    <hr>
    <form class="create_game" @submit.prevent="createGame()">
        <textarea placeholder="Название игры" id="create_game_input" class="form-control create_game_input"></textarea>
        <input type="submit" value="Создать игру" class="btn btn-primary create_game_button">
      </form>
    <hr>
      <h1>Доступные игры</h1> 
      <div class="games_list">
          <p class="game_title" v-for="game in game_list" :key="game.id" @click="pushToGame(game.id)">
              Зайти в игру: {{game.title}}
          </p>
      </div>
      
  </div>
</template>

<script>
import axios from 'axios'
import {mapState} from 'vuex'
export default {
    name: 'Main',
    data(){
        return{
            game_list: []
        }
    },
    created(){
        document.title = this.$route.meta.title;
    },
    mounted(){
        this.getGameList()
    },
    computed: mapState(['username']),
    methods:{
        getGameList(){
            axios.get('http://127.0.0.1:8000/api/game/list/', {headers:{Authorization: `Bearer ${this.$store.state.accessToken}`}})
            .then(responce=>{
                this.game_list = responce.data
            })
            .catch(err=>{
                console.log(err)
            })
        },
        pushToGame(id){
            this.$router.push({path: 'game', query: {'gameId': id}})
        },
        createGame(){
            axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/api/game/list/',
                headers:{
                    Authorization: `Bearer ${this.$store.state.accessToken}`
                },
                data:{
                    title: document.querySelector('#create_game_input').value,
                    user_name_1: this.username
                }
            })
            .then((responce)=>{
                this.game_list.push(responce.data)
                document.querySelector('#create_game_input').value = ''
            })
        }
    }
}
</script>

<style>
.create_game_button{
    margin-top: 20px;
}

.games_list{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center
}

.game_title{
    margin-top: 10px;
    width: 300px;
}
</style>