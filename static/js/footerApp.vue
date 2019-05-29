<template>
  <div>{{footerTitle}}</div>
</template>

<script>
module.exports = {
  data () {
    return {
      footerTitle: 'T U N A S T R E A M'
    }
  }
}
</script>

<style scoped>
#footer {
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-shrink: 0;

    height: 50px;
    background-color: aliceblue;
    padding-left: 10px;
}
</style>

