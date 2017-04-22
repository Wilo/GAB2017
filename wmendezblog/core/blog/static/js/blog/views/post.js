inPlanet.Views.PostView = Marionette.ItemView.extend({
 tagName: "section",
 template: Handlebars.compile($("#post-template").html()) //"#post-template"
});
