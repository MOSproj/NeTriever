(function(){
    "use strict";

    angular.module('myApp').controller('postsCtrl', ["$scope", "postsSrv","$routeParams", postsCtrl]);

    function postsCtrl ($scope, postsSrv, $routeParams) {
        var self = this;
        self.cat = $routeParams.category;
        postsSrv.getPosts($routeParams.category).then(function (response) {
            console.log(response);
            self.posts = response.data;
        });
    }
})();
