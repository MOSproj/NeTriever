(function(){
    "use strict";

    angular.module('myApp').controller('postsCtrl', ["$scope", "$routeParams", "$location", "$log", "categoriesSrv", "postsSrv", postsCtrl]);

    function postsCtrl ($scope, $routeParams, $location, $log, categoriesSrv, postsSrv) {
        var self = this;
        var reqParams = $location.search();

        self.categoryId = $routeParams['categoryId'];
        categoriesSrv.getCategory(self.categoryId).then(function (response) {
            $log.debug(response.data);

            self.category = response.data;

            self.category['specRange'] = {};
            self.category['specselect'] = {};
            angular.forEach(self.category['specs'], function(specValues, speckey) {
                if (angular.isArray(specValues)) {
                    var data = [];
                    specValues.forEach(function (value, i){
                        data.push({
                            'id': i,
                            'label': value
                        });
                    });
                    self.category['specselect'][speckey] = {
                        'data': data,
                        'selected': []
                    };
                } else
                    self.category['specRange'][speckey] = specValues;
            });
            $log.log(self.category['specRange']);
            $log.log(self.category['specselect']);
        });

        self.postsPerPage = 50;

        postsSrv.getPosts(self.categoryId, reqParams).then(function (response) {
            $log.debug(response.data);

            self.posts = response.data;
        });

        self.pagination = {
            backButtonDisabled: function () {
                return !reqParams.hasOwnProperty('page') || reqParams['page'] === "1";
            },
            forwardButtonDisabled: function () {
                return self.posts !== undefined && self.posts.length !== self.postsPerPage;
            },
            back: function () {
                if (!self.pagination.backButtonDisabled()) {
                    reqParams['page'] = reqParams['page'] - 1;
                    $location.path($location.path()).search(reqParams);
                }
            },
            forward: function () {
                if (!self.pagination.forwardButtonDisabled()) {
                    if (!reqParams.hasOwnProperty('page'))
                        reqParams['page'] = 1;
                    reqParams['page'] = reqParams['page'] + 1;

                    $location.path($location.path()).search(reqParams);
                }
            }
        };

        self.isString = function(item) {
            return angular.isString(item);
        };
    }
})();
