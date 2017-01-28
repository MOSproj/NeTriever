var express = require('express');
var app = express();
var mongojs = require('mongojs');
// TODO create and use user with restrictions
var db = mongojs('test', ['categories', 'groups', 'posts']);
var bodyParser = require('body-parser');

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());

db.on('error', function (err) {
    console.log('database error', err)
});

db.on('connect', function () {
    console.log('database connected')
});

app.get('/categories', function (req, res) {
    db.categories.find({}, function (err, docs) {
        console.log(docs);
        res.json(docs);
    });
});

/*app.get('/posts', function (req, res) {
    db.posts.find({}, function (err, docs) {
        console.log(docs);
        res.json(docs);
    });
});*/

app.get('/posts', function (req, res) {
    var category = req.query.category;
    console.log(category);
    console.log(category);
    if(category == "") {
        db.posts.find({}, function (err, docs) {
            console.log(docs);
            res.json(docs);
        });
    } else {
        db.groups.find({'category': category}, function (err, docs) {
            console.log(docs);
        });
    }
});

app.listen(3000);