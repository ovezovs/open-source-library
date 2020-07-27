var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var GenreSchema = new Schema(
  {
    name: {type: String, required: true, max: 100},
  }
);

// Virtual for bookinstance's URL
GenreSchema
.virtual('url')
.get(function () {
  return '/home/genre/' + this._id;
});

//Export model
module.exports = mongoose.model('Genre', GenreSchema);