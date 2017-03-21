var express = require('express');
var app = express();
var mongojs = require('mongojs');
var config = require('./config');
var bodyParser = require('body-parser');

var dbFullPath = '';
if(config.username != '')
    dbFullPath += config.username + ':' + config.password + '@';
if(config.dbPath != '')
    dbFullPath += config.dbPath + '/';
dbFullPath += config.dbName;

var db = mongojs(dbFullPath, ['categories', 'groups', 'posts']);

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());


db.on('error', function (err) {
    console.log('database error', err)
});

db.on('connect', function () {
    console.log('database connected')
});

app.use('/scripts', express.static(__dirname + '/node_modules/'));

app.get('/get-categories', function (req, res) {
    db.categories.find({}, function (err, docs) {
        console.log(docs);
        res.json(docs);
    });
});

app.get('/get-posts', function (req, res) {
    db.posts.find({}, function (err, docs) {
        console.log(docs);
        res.json(docs);
    });
});

app.get('/get-posts/:category', function (req, res) {
    var category = req.params.category;
    console.log(category + " category");
    console.log(req);
    db.groups.find({'category': category}, function (err, docs) {
        console.log(docs);
    });
});

/* Fixing angular routing */
/* http://stackoverflow.com/questions/29741759/node-js-404-and-angular-url-refresh-conflict */
app.use('/*', function (req, res) {
   res.sendFile(__dirname + '/public/index.html');
});

app.use(function(req, res) { //put this at end
    res.status(404);//add this line for setting 404 status
    res.render('404', {layout: false, title: '404: File Not Found'});
});

app.listen(3000);
