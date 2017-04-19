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
    }
})();
