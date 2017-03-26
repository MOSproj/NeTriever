(function(){
    "use strict";

    angular.module('myApp').controller('postsCtrl', ["$scope", "$routeParams", "$log", "postsSrv", postsCtrl]);

    function postsCtrl ($scope, $routeParams, $log, postsSrv) {
        var self = this;
        self.categoryName = $routeParams.category;
        postsSrv.getPosts($routeParams.category).then(function (response) {
            $log.debug(response.data);

            self.posts = response.data;
        });
    }
})();
