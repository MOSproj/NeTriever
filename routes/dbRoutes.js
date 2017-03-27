var express = require('express');
var router = express.Router();
var mongojs = require('mongojs');
var config = require('../config');

var dbFullPath = '';
if(config.username !== '')
    dbFullPath += config.username + ':' + config.password + '@';
if(config.dbPath !== '')
    dbFullPath += config.dbPath + '/';
dbFullPath += config.dbName;

var db = mongojs(dbFullPath, ['categories', 'groups', 'posts2']);
db.on('error', function (err) {
    console.log('database error:', err)
});
db.on('connect', function () {
    console.log('database connected')
});

var getCategoriesName =  function (res) {
    // TODO: add proxy
    db.categories.find({}, {"name":1,_id:0}, function (err, docs) {
        res(docs);
    });
};

var getCategoryByName = function (categoryName, res) {
    // TODO: add proxy
    db.categories.findOne({'name': categoryName}, function (err, docs) {
        res(docs);
    });
};

var getGroupsByCategory = function (category, res) {
    // TODO: add proxy
    db.groups.find({'category.$id': category._id}, function (err, docs) {
        res(docs);
    });
};

var getPostsByGroups = function (groups, res) {
    var groupsIds = [];
    groups.forEach(function(group) {
        groupsIds.push(group.id);
    });
    db.posts2.find({'group_id': {'$in': groupsIds}}, function (err, docs) {
        res(docs);
    });
};

router.get('/categories-names', function (req, res) {
    getCategoriesName(function (categoriesName) {
        res.json(categoriesName);
    });
});

router.get('/posts/:category', function (req, res) {
    var categoryName = req.params.category;
    console.log(categoryName + " category");
    getCategoryByName(categoryName, function (category) {
        getGroupsByCategory(category, function (groups) {
            getPostsByGroups(groups, function (posts) {
                res.json(posts);
            });
        });
    });
});

module.exports = router;