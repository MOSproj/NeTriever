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
            self.categoryName = self.category['name'];
            self.categoryspecs = self.category['specs'];
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
    }
})();
