(function(){
    "use strict";

    angular.module('myApp').controller('postsCtrl', ["$scope", "$routeParams", "$location", "$log", "postsSrv", postsCtrl]);

    function postsCtrl ($scope, $routeParams, $location, $log, postsSrv) {
        var self = this;
        var reqParams = $location.search();

        self.categoryName = $routeParams['category'];
        self.postsPerPage = 50;

        postsSrv.getPosts(self.categoryName, reqParams).then(function (response) {
            $log.debug(response.data);

            self.posts = response.data;
        });

        self.pagination = {
            backButtonDisabled: function () {
                return !reqParams.hasOwnProperty('page') || reqParams['page'] === "1";
            },
            forwardButtonDisabled: function () {
                return self.posts.length !== self.postsPerPage;
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
