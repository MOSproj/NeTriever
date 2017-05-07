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
    console.log('database connected');
});

var getGroupsByCategoryId = function (categoryId, res) {
    db.groups.find({'category_id': categoryId}, function (err, docs) {
        res(docs);
    });
};

var getCategories = function (res) {
    db.categories.find({})
        .sort({'id': 1}, function (err, docs) {
        res(docs);
    });
};

var getCategoriesName =  function (res) {
    db.categories.find({}, {'name':1, 'id':1})
        .sort({'id': 1}, function (err, docs) {
        res(docs);
    });
};

var getPosts = function (groups, queryData, pageNum, res) {
    var then = new Date();
    var groupsIds = [];

    groups.forEach(function(group) {
        groupsIds.push(group.id);
    });

    var mongoDbReq = createMongoDbReq(queryData);
    mongoDbReq.push({'group_id': {'$in': groupsIds}});
    console.log(JSON.stringify({'$and': mongoDbReq}));

    db.posts.find({'$and': mongoDbReq})
        .sort({'updated_time': -1})
        .skip(postsPerPage*(pageNum-1))
        .limit(postsPerPage, function (err, docs) {
            console.log(new Date() - then);
            console.log((new Date).toISOString());
            res(docs);
        });
};

var createMongoDbReq = function (queryData) {
    var answer = [];

    if (queryData.hasOwnProperty('מחיר')) {
        answer.push({'price': { '$gt': queryData['מחיר'].split("-")[0],
                                '$lt': queryData['מחיר'].split("-")[1]}
        });
        delete queryData['מחיר'];
    }
    if (queryData.hasOwnProperty('מיקום')) {
        answer.push({'location': {'$in': queryData['מיקום']}});
        delete queryData['מיקום'];
    }

    Object.keys(queryData).forEach(function(key) {
        if (Array.isArray(queryData[key])){
            var toInsert = {};
            toInsert['specs.' + key] = {'$in': queryData[key]};
            answer.push(toInsert);
        } else {
            //TODO: 1 choice
            var toInsert = {};
            toInsert['specs.' + key] = {    '$gt': queryData[key].split("-")[0],
                                            '$lt': queryData[key].split("-")[1]};
            answer.push(toInsert);
        }
    });
    return answer;
};

router.get('/categories', function (req, res) {
    getCategories(function (categories) {
        res.json(categories);
    });
});

router.get('/categories-names', function (req, res) {
    getCategoriesName(function (categoriesName) {
        res.json(categoriesName);
    });
});

router.get('/category/:categoryId', function (req, res) {
    console.log(req.params['categoryId']);
    const categoryId = parseInt(req.params['categoryId']);

    db.categories.findOne({'id': categoryId}, function (err, docs) {
        res.json(docs);
    });
});

router.get('/posts/:categoryId', function (req, res) {
    console.log(req.params['categoryId']);
    const categoryId = parseInt(req.params['categoryId']);
    console.log(categoryId + " category");
    var queryData = req.query;

    var pageNum = 1;
    if (queryData.hasOwnProperty('page')) {
        pageNum = queryData['page'];
        delete queryData['page'];
    }

    getGroupsByCategoryId(categoryId, function (groups) {
        getPosts(groups, queryData, pageNum, function (posts) {
            res.json(posts);
        });
    });
});

module.exports = router;
