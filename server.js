var express = require('express');
var app = express();
var mongojs = require('mongojs');
var config = require('./config');

var dbFullPath = '';
if(config.username != '')
    dbFullPath += config.username + ':' + config.password + '@';
if(config.dbPath != '')
    dbFullPath += config.dbPath + '/';
dbFullPath += config.dbName;

var db = mongojs(dbFullPath, ['categories', 'groups', 'posts']);
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

app.get('/posts', function (req, res) {
    db.posts.find({}, function (err, docs) {
        console.log(docs);
        res.json(docs);
    });
});

app.get('/posts/:category', function (req, res) {
    var category = req.params.category;
    console.log(category + " category");
    db.groups.find({'category': category}, function (err, docs) {
        console.log(docs);
    });
});

app.listen(3000);
