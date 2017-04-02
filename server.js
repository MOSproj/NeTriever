var express = require('express');
var mongojs = require('mongojs');
var bodyParser = require('body-parser');

var apiRoutes = require('./routes/apiRoutes');

var app = express();

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());
app.use('/scripts', express.static(__dirname + '/node_modules/'));

app.use('/api/', apiRoutes);

/* Fixing angular routing */
/* http://stackoverflow.com/questions/29741759/node-js-404-and-angular-url-refresh-conflict
app.use('/*', function (req, res) {
   res.sendFile(__dirname + '/public/index.html');
});*/

app.use('/category/*', function (req, res) {
    res.sendFile(__dirname + '/public/index.html');
});

app.use(function(req, res) { //put this at end
    res.status(404);//add this line for setting 404 status
    res.render('404', {layout: false, title: '404: File Not Found'});
});

app.listen(3000);
