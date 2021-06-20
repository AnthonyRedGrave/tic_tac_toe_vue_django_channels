<template>
  <div class="box" @click="boxPressed(item.id)">
      <div class="item" v-if="item.x == true">x</div>
      <div class="item" v-if="item.o == true">o</div>
  </div>
</template>

<script>
export default {
    name: 'Box',
    props:{
        item:{
            type: Object,
            default: ()=>{}
        },
        gameEnd:{
            type: Boolean
        }
    },
    methods:{
        boxPressed(id){
            if(this.gameEnd === false){
                this.$emit('selectBox', id)
            }
            

        }
    }
}
</script>

<style>
    .box{
        width: 100px;
        height: 100px;
        border: 1px solid black;
        box-sizing: border-box;
        font-size: 34px;
        color: brown;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>