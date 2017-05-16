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
            console.log('request took ' + (new Date() - then) + 'ms to answer on '
                + (new Date).toISOString());
            res(docs);
        });
};

var createMongoDbReq = function (queryData) {
    var answer = [];

    if (queryData.hasOwnProperty('מחיר')) {
        var price = {};
        if (parseInt(queryData['מחיר'].split(",")[0]) >= 0)
            price['$gt'] = parseInt(queryData['מחיר'].split(",")[0]) - 1;
        if (parseInt(queryData['מחיר'].split(",")[1]) >= 0)
            price['$lt'] = parseInt(queryData['מחיר'].split(",")[1]) + 1;
        answer.push({'price': price});
        delete queryData['מחיר'];
    }
    if (queryData.hasOwnProperty('מיקום')) {
        answer.push({'location': {'$in': [].concat(queryData['מיקום'])}});
        delete queryData['מיקום'];
    }

    Object.keys(queryData).forEach(function(key) {
        var toInsert = {};
        if (queryData[key].includes(',')){
            toInsert['specs.' + key] = {};
            if (parseFloat(queryData[key].split(",")[0]) >= 0)
                toInsert['specs.' + key]['$gt'] = parseFloat(queryData[key].split(",")[0]) - 0.1;
            if (parseFloat(queryData[key].split(",")[1]) >= 0)
                toInsert['specs.' + key]['$lt'] = parseFloat(queryData[key].split(",")[1]) + 0.1;
        } else {
            toInsert['specs.' + key] = {'$in': [].concat(queryData[key])};
        }
        answer.push(toInsert);
    });
    return answer;
};

router.get('/categories', function (req, res) {
    console.log('/categories');
    getCategories(function (categories) {
        res.json(categories);
    });
});

router.get('/categories-names', function (req, res) {
    console.log('/categories-names');

    getCategoriesName(function (categoriesName) {
        res.json(categoriesName);
    });
});

router.get('/category/:categoryId', function (req, res) {
    const categoryId = parseInt(req.params['categoryId']);
    console.log('/category/' + categoryId);

    db.categories.findOne({'id': categoryId}, function (err, docs) {
        docs['specs'] = Object.assign({
            'מיקום': cities
        }, docs['specs']);
        res.json(docs);
    });
});

router.get('/posts/:categoryId', function (req, res) {
    const categoryId = parseInt(req.params['categoryId']);
    console.log("/posts/" + categoryId);
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

var cities = [
    "אופקים", "אור יהודה", "אור עקיבא", "אילת", "אלעד", "אריאל", "אשדוד", "אשקלון", "באר שבע", "בית שאן", "בית שמש",
    "ביתר עילית", "בני ברק", "בת ים", "גבעת שמואל", "גבעתיים", "דימונה", "הוד השרון", "הרצליה", "חדרה", "חולון", "חיפה",
    "טבריה", "טייבה", "טירה", "טירת כרמל", "טמרה", "יבנה", "יהוד-מונוסון", "יקנעם עילית", "ירושלים", "כפר יונה",
    "כפר סבא", "כפר קאסם", "כרמיאל", "לוד", "מגדל העמק", "מודיעין עילית", "מודיעין- מכבים- רעות", "מעלה אדומים",
    "מעלות תרשיחא", "נהריה", "נס ציונה", "נצרת", "נצרת עילית", "נשר", "נתיבות", "נתניה", "סח'נין", "עכו", "עפולה",
    "עראבה", "ערד", "פתח תקווה", "צפת", "קלנסווה", "קריית אונו", "קריית אתא", "קריית ביאליק", "קריית גת", "קריית ים",
    "קריית מוצקין", "קריית מלאכי", "קריית שמונה", "ראש העין", "ראשון לציון", "רהט", "רחובות", "רמלה", "רמת גן",
    "רמת השרון", "רעננה", "שדרות", "שפרעם", "תל אביב יפו"
];
