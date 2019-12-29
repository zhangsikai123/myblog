new Vue({
  el: '#post-container',
  data: {
    input: document.getElementById('post-full').getAttribute('data-repo')
  },
  computed: {
    compiledMarkdown: function () {
      return marked(this.input, { sanitize: true })
    }
  },
  methods: {
    update: _.debounce(function (e) {
      this.input = e.target.value
    }, 300)
  }
});
