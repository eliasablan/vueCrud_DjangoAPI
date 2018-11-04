<template>
  <div class="posts">
    <h1 v-if="post.id!=null">Editar Entrada</h1>
    <h1 v-else>Agregar Entrada</h1>
    <form action="" method="post">

      <p>
        <label for="title">Titulo </label>
        <input type="text" id="title" name="title" v-model="post.title" @keyup="createSlug">
      </p>

      <p>
        <label for="slug">Slug </label>
        <input type="text" readonly id="slug" name="slug" v-model="post.slug" placeholder="slug">
      </p>

      <p>
        <label for="">Estado </label>
        <select class="" name="status" v-model="post.status">
          <option value="D">Borrador</option>
          <option value="P">Publicado</option>
        </select>
      </p>

      <p>
        <label for="category">Categoria </label>
        <select class="" name="category" v-model="post.category">
          <option v-for="category in categories" :value="category.id">{{category.name}}</option>
        </select>
      </p>

      <p>
        <label for="content">Contenido </label>
        <textarea id="content" name="content" rows="8" cols="80" v-model="post.content"></textarea>
      </p>

      <p>
        <label for="image">Imagen </label>
        <input type="file" @change="onFileSelected">
      </p>
      <p v-if="post.image">
        <img :src="post.image_450" alt="">
      </p>

      <p>
        <label for="autor">Autor </label>
        <select class="" name="author" v-model="post.author">
          <option v-for="author in authors" :value="author.id">{{author.name}}</option>
        </select>
      </p>

      <br>

      <button v-if="post.id!=null" @click.prevent="savePost" type="button" name="button">Editar</button>
      <button v-else @click.prevent="savePost" type="button" name="button">Crear</button>

    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'post-create',
  mounted() {

    var id = this.$route.params.id

    if(id!=null) {
      axios.get('http://127.0.0.1:8000/api/publicaciones/'+id)
      .then((respuesta) => {
        this.post = respuesta.data
      })
    }

    axios.get('http://127.0.0.1:8000/api/autores/')
    .then((respuesta) => {
      this.authors=respuesta.data
    })
    axios.get('http://127.0.0.1:8000/api/categorias/')
    .then((respuesta) => {
      this.categories=respuesta.data
    })
  },
  data() {
    return {
      authors: [],
      categories: [],
      post: {
        id: null,
        title: '',
        slug: 'slug',
        status: '',
        category: null,
        content: '',
        image: null,
        author: null
      }
    }
  },
  methods: {
    createSlug: function () {

      var slug = this.post.title.toLowerCase()

      slug = slug.replace(/á|à|ả|ạ|ã|ă|ắ|ằ|ẳ|ẵ|ặ|â|ấ|ầ|ẩ|ẫ|ậ/gi, 'a')
      slug = slug.replace(/é|è|ẻ|ẽ|ẹ|ê|ế|ề|ể|ễ|ệ/gi, 'e')
      slug = slug.replace(/i|í|ì|ỉ|ĩ|ị/gi, 'i')
      slug = slug.replace(/ó|ò|ỏ|õ|ọ|ô|ố|ồ|ổ|ỗ|ộ|ơ|ớ|ờ|ở|ỡ|ợ/gi, 'o')
      slug = slug.replace(/ú|ù|ủ|ũ|ụ|ư|ứ|ừ|ử|ữ|ự/gi, 'u')
      slug = slug.replace(/ý|ỳ|ỷ|ỹ|ỵ/gi, 'y')
      slug = slug.replace(/đ/gi, 'd')
      slug = slug.replace(/\`|\~|\!|\@|\#|\||\$|\%|\^|\&|\*|\(|\)|\+|\=|\,|\.|\/|\?|\>|\<|'|\"|\:|\;|_/gi, '')
      slug = slug.replace(/ /gi, "-")
      slug = slug.replace(/\-\-\-\-\-/gi, '-')
      slug = slug.replace(/\-\-\-\-/gi, '-')
      slug = slug.replace(/\-\-\-/gi, '-')
      slug = slug.replace(/\-\-/gi, '-')
      slug = '@' + slug + '@'
      slug = slug.replace(/\@\-|\-\@|\@/gi, '')

      this.post.slug = slug
    },
    onFileSelected: function(e) {
      this.post.image = e.target.files[0]
    },
    savePost: function() {

      var data = {
        title: this.post.title,
        slug: this.post.slug,
        status: this.post.status ? this.post.status : "D",
        category: this.post.category,
        content: this.post.content,
        image: this.post.image,
        author: this.post.author
      }

      var router = this.$router

      if(this.post.id!=null) {
        axios.put('http://127.0.0.1:8000/api/publicaciones/'+this.post.id+'/', data)
        .then((respuesta) => {
          if(respuesta.status==200 || respuesta.statusText=='OK') {
            router.push({name:"posts"})
          }
          else {
            console.log("error" + respuesta.data)
            alert("error al editar la entrada")
          }
        })
        .catch((error) => {
          console.log(error.response)
        })
      }
      else {
        axios.post('http://127.0.0.1:8000/api/publicaciones/', data)
        .then((respuesta) => {
          if(respuesta.status==201 || respuesta.statusText=='Created') {
            router.push({name:"posts"})
          } else {
            console.log("error" + respuesta.data)
            alert("error al crear la entrada")
          }
        })
        .catch((error) => {
          console.log(error.response)
        })
      }
    }
  }
}
</script>

<style lang="css">
</style>
