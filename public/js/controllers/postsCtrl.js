(function(){
    "use strict";

    angular.module('myApp').controller('postsCtrl', ["$scope", "$routeParams", "$log", "postsSrv", postsCtrl]);

    function postsCtrl ($scope, $routeParams, $log, postsSrv) {
        var self = this;
        self.categoryName = $routeParams.category;
        self.pageNum = parseInt($routeParams.page);
        self.postsPerPage = 50;

        postsSrv.getPosts(self.categoryName, self.pageNum).then(function (response) {
            $log.debug(response.data);

            self.posts = response.data;
        });
    }
})();
