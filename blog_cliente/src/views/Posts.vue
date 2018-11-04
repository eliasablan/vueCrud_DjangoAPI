<template>
  <div class="posts">
    <h1>Listado de Entradas</h1>
    <router-link :to="{name:'post-create'}">Nueva Publicación</router-link>

    <table id="tabla">
      <tr>
        <th>index</th>
        <th>TITULO</th>
        <th>AUTOR</th>
        <th>CATEGORIA</th>
        <th>ESTADO</th>
        <th>OPCIONES</th>
      </tr>
      <tr v-for="(post, index) in posts">
        <td>{{index+1}}</td>
        <td>{{post.title}}</td>
        <td>{{post.authorName}}</td>
        <td>{{post.categoryName}}</td>
        <td v-if="post.status=='P'">Publicado</td>
        <td v-if="post.status=='D'">Borrador</td>
        <td>
          <router-link :to="{name:'post-edit',params:{id:post.id}}">Editar</router-link>
          <span> | </span>
          <a @click.prevent="deletePost(post.id)" href="#">Eliminar</a>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'posts',
  mounted() {
    this.cargarEntradas()
  },
  data() {
    return {
      posts:[]
    }
  },
  methods: {
    cargarEntradas: function() {
      axios.get('http://127.0.0.1:8000/api/publicaciones/')
      .then((respuesta) => {
        this.posts=respuesta.data
      })
    },
    deletePost: function(id) {

      var op = window.confirm("¿Esta seguro de eliminar la entrada?")

      if(op) {
        axios.delete('http://127.0.0.1:8000/api/publicaciones/'+id+'/')
        .then((respuesta) => {
          console.log(respuesta)
          this.cargarEntradas()
        })
      }
    }
  }
}
</script>

<style lang="css">
table, th, td {
  margin: 10px auto;
}
th {
  background-color: #42b983;
  color: white;
}
th, td {
  padding: 5px;
}
tr:hover {
  background-color: #f5f5f5;
}
</style>
