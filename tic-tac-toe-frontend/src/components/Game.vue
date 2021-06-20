<template>
  <div class="v-game block">
      Игра
      <div class="area-wrapper">
          <div id="area">
              <Box
              v-for="box in fields" :key="box.id" :item="box" :gameEnd="isGameEnd" @selectBox="selectBox($event)"/>
          </div>
          
          
      </div>
      <div class="gameStatus">
        {{gameStatus}}
      </div>
  </div>
</template>

<script>
import Box from '@/components/Box.vue'
export default {
    name: 'Game',
    components:{
        Box
    },
    data(){
        return{
            fields: [],
            gameStatusInt: 1,
            gameStatus: null,
            isGameEnd: false
        }    
    },
    mounted(){
        this.gameInit()
    },
    methods:{
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
</style>