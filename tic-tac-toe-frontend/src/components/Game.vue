<template>
  <div class="v-game block">
      <div class="left_menubar">
          <p>Пользователь 1: {{user_1}}</p> 
          <p>Пользователь 2: {{user_2}}</p> 
          <p>Результат игры: </p> 
      </div>
      Игра <b>{{title}}</b>
      <br>
      <br>
      <div class="area-wrapper">
          <div id="area">
              <Box
              v-for="box in fields" :key="box.id" :item="box" :user2IsReady="user2IsReady" :gameEnd="isGameEnd" @selectBox="selectBox($event)"/>
          </div>
          
          
      </div>
      <div class="gameStatus">
        {{gameStatus}}
      </div>
      <div v-if="user2IsReady===false" class="user2IsReady">
          Подождите второго игрока
      </div>
      <div class="gameStart">
          Второй игрок подключился!
          Начинайте игру!
      </div>
  </div>
</template>

<script>
import Box from '@/components/Box.vue'
import axios from 'axios'
export default {
    name: 'Game',
    components:{
        Box
    },
    data(){
        return{
            fields: [],
            title:null,
            user_1: null,
            user_2: null,
            gameStatusInt: 1,
            gameStatus: null,
            isGameEnd: false,
            user2IsReady: false,
            user1Step: false,
            user2Step: false
        }
    },
    created(){
        document.title = this.$route.meta.title;
        this.socket = new WebSocket(
        'ws://'+
        'localhost:8000' +
        '/ws/game/' +
        this.$route.query.gameId +
        '/'
        )

        this.socket.onopen = function(){
        }
        let _this = this
        this.socket.onmessage = function(event){
            let data = JSON.parse(event.data)
            if(data['user2IsReady_send'] === true){
                console.log("можно играть")
                _this.user2IsReady = true
                document.querySelector('.user2IsReady').style.display = 'none'
                document.querySelector('.gameStart').style.display = 'block'
                setTimeout(function(){
                    document.querySelector('.gameStart').style.display = 'none'
                }, 3000);
                _this.user1Step = true
                
            }
        }
        this.getGameInfo()
        
    },
    mounted(){
        this.gameInit()
    },
    methods:{
        getGameInfo(){
            axios.get(`http://127.0.0.1:8000/api/game/list/${this.$route.query.gameId}`, {headers:{Authorization: `Bearer ${this.$store.state.accessToken}`}})
            .then((responce)=>{
                this.title =  responce.data.title,
                this.user_1 = responce.data.user_name_1,
                this.user_2 = responce.data.user_name_2
            })
        },
        gameInit(){
            for (let i=0;i<9;i++){
                let item = {id: i,
                        x: false,
                        o: false}
                this.fields.push(item)
            }
        },
        selectBox(id){
            if (this.gameStatusInt == 1 || this.gameStatusInt%2==1){
                this.fields[id].x = true
                
            }
            else if(this.gameStatusInt%2==0){
                this.fields[id].o = true
                
            }
            this.gameStatusInt++
            if(this.gameStatusInt >= 6){
                this.checkGameStatus()
            }
            
        },
        checkGameStatus(){
            if((this.fields[0].x === true && this.fields[1].x === true && this.fields[2].x === true) || (this.fields[0].o === true && this.fields[1].o === true && this.fields[2].o === true)){
                this.gameStatus = "Победа по горизонтали"

                    this.isGameEnd = true
                    if(this.isGameEnd){
                        return 
                    }
            }
            else if((this.fields[3].x === true && this.fields[4].x === true && this.fields[5].x === true) || (this.fields[3].o === true && this.fields[4].o === true && this.fields[5].o === true)){
                this.gameStatus = "Победа по горизонтали"

                    this.isGameEnd = true
                    if(this.isGameEnd){
                        return 
                    }
            }
            else if((this.fields[6].x === true && this.fields[7].x === true && this.fields[8].x === true) || (this.fields[6].o === true && this.fields[7].o === true && this.fields[8].o === true)){
                this.gameStatus = "Победа по горизонтали"

                    this.isGameEnd = true
                    if(this.isGameEnd){
                        return 
                    }
            }
            else if((this.fields[0].x === true && this.fields[3].x === true && this.fields[6].x === true) || (this.fields[0].o === true && this.fields[3].o === true && this.fields[6].o === true)){
                this.gameStatus = "Победа по вертикали"

                    this.isGameEnd = true
                    if(this.isGameEnd){
                        return 
                    }
            }
            else if((this.fields[1].x === true && this.fields[4].x === true && this.fields[7].x === true) || (this.fields[1].o === true && this.fields[4].o === true && this.fields[7].o === true)){
                this.gameStatus = "Победа по вертикали"

                    this.isGameEnd = true
                    if(this.isGameEnd){
                        return 
                    }
            }
            else if((this.fields[2].x === true && this.fields[5].x === true && this.fields[8].x === true) || (this.fields[2].o === true && this.fields[5].o === true && this.fields[8].o === true)){
                this.gameStatus = "Победа по вертикали"

                    this.isGameEnd = true
                    if(this.isGameEnd){
                        return 
                    }
            }
            else if((this.fields[0].x === true && this.fields[4].x === true && this.fields[8].x === true) || (this.fields[0].o === true && this.fields[4].o === true && this.fields[8].o === true)){
                this.gameStatus = "Победа по диагонали"

                    this.isGameEnd = true
                    if(this.isGameEnd){
                        return 
                    }
            }
            else if((this.fields[2].x === true && this.fields[4].x === true && this.fields[6].x === true) || (this.fields[2].o === true && this.fields[4].o === true && this.fields[6].o === true)){
                this.gameStatus = "Победа по диагонали"

                    this.isGameEnd = true
                    if(this.isGameEnd){
                        return 
                    }
            }
        }
    }

}
</script>

<style>
    .area-wrapper{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    #area{
        width: 300px;
        height: 300px;
        background-color: blanchedalmond;
        display: flex;
        flex-wrap: wrap;

    }

    .left_menubar{
        position: absolute;
        background-color: #c0c0c0;
        padding: 30px;
    }

    .gameStart{
        display: none;
    }
</style>