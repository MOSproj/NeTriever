var express = require('express');
var app = express();
var mongojs = require('mongojs');
var db = mongojs('test', ['categories', 'groups', 'posts']);

app.use(express.static(__dirname + '/public'));

db.on('error', function (err) {
    console.log('database error', err)
});
db.on('connect', function () {
    console.log('database connected')
});

app.get('/posts', function (req, res) {
    db.posts.find({}, function (err, docs) {
        console.log(docs);
        res.json(docs);
    });
});

app.listen(3000);