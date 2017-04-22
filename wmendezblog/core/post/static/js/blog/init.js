/*var inPlanet = {};
inPlanet.Collections = {};
inPlanet.Models = {};
inPlanet.Views = {};
inPlanet.Routers = {};
inPlanet.Regions = {};

inPlanet = new Marionette.Application()
*/
//init.js
var inPlanet = {};
inPlanet.App = {};
inPlanet.Collections = {};
inPlanet.Models = {};
inPlanet.Views = {};
inPlanet.Routers = {};
inPlanet.Regions = {};


window.inplanet = {};

inPlanet.App = new Marionette.Application()
  //regions.js
inPlanet.App.addRegions({
  mainRegion: "#post"
});

//models.js
/*
var postModel = Backbone.Model.extend();

inPlanet.App.Models.Post= new postModel();

//collections.js
var PostsCollection = Backbone.Collection.extend({
  url: '/api/post',
  model: inPlanet.Models.Post,
  initialize: function(){
    this.fetch();
  },
});

inPlanet.Collections.Post = new PostsCollection();
//app.js
console.log(inPlanet.Collections.Post);

inPlanet.App.on("start", function(){
			console.log(inPlanet.Collections );
})
inPlanet.App.start();
*/
