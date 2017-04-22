var PostsCollection = Backbone.Collection.extend({
  url: '/api/post',
  model: inPlanet.Models.Post,
  initialize: function(){
    this.fetch();
  },
});

inPlanet.Collections.Posts = new PostsCollection();
