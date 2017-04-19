var express = require('express');
var router = express.Router();
var mongojs = require('mongojs');
var config = require('../config');

const postsPerPage = 50;

var uri = '';
if(config.username !== '')
    uri += config.username + ':' + config.password + '@';
if(config.dbPath !== '')
    uri += config.dbPath;
const collections = ['categories', 'groups', 'posts'];

var db = mongojs(uri, collections);
db.on('error', function (err) {
    console.log('database error:', err)
});
db.on('connect', function () {
    console.log('database connected')
});


var getCategoriesName =  function (res) {
    db.categories.find({}, {"name":1,_id:0}, function (err, docs) {
        res(docs);
    });
};

var getCategoryByName = function (categoryName, res) {
    db.categories.findOne({'name': categoryName}, function (err, docs) {
        res(docs);
    });
};

var getGroupsByCategory = function (category, res) {
    db.groups.find({'category.$id': category._id}, function (err, docs) {
        res(docs);
    });
};

var getPostsByGroups = function (groups, pageNum, res) {
    var then = new Date();
    var groupsIds = [];
    groups.forEach(function(group) {
        groupsIds.push(group.id);
    });
    db.posts.find({'group_id': {'$in': groupsIds}})
        .sort({'updated_time': -1})
        .skip(postsPerPage*(pageNum-1))
        .limit(postsPerPage, function (err, docs) {
            console.log(new Date() - then);
            console.log((new Date).toISOString());
            res(docs);
        });
};

router.get('/categories-names', function (req, res) {
    getCategoriesName(function (categoriesName) {
        res.json(categoriesName);
    });
});

router.get('/category/:category', function (req, res) {
    const categoryName = req.params['category'];
    console.log(categoryName + " category");

    var pageNum = 1;
    if (req.query.hasOwnProperty('page'))
        pageNum = req.query['page'];


    getCategoryByName(categoryName, function (category) {
        getGroupsByCategory(category, function (groups) {
            getPostsByGroups(groups, pageNum, function (posts) {
                res.json(posts);
            });
        });
    });
});

module.exports = router;
