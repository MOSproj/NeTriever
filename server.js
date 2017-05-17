var express = require('express');
var mongojs = require('mongojs');
var bodyParser = require('body-parser');

var apiRoutes = require('./routes/apiRoutes');

var app = express();
app.set('view engine', 'html');

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());
app.use('/scripts', express.static(__dirname + '/node_modules/'));

app.use('/api/', apiRoutes);

app.use('/category/*', function (req, res) {
    res.sendFile(__dirname + '/public/index.html');
});

app.use('/מועדפים', function (req, res) {
    res.sendFile(__dirname + '/public/index.html');
});

app.use('/404', function (req, res) {
    res.sendFile(__dirname + '/public/index.html');
});

app.use(function(req, res) { //put this at end
    console.log('404 page');
    res.status(404);
    res.redirect('/404');
});

app.listen(3000);
