(function(){
    "use strict";

    angular.module('myApp').controller('likesCtrl', ["$scope", "$routeParams", "$location", "$log", "postsSrv",
        "cookiesSrv", likesCtrl]);

    function likesCtrl ($scope, $routeParams, $location, $log, postsSrv, cookiesSrv) {
        var self = this;
        var reqParams = $location.search();

        self.cookieObj = cookiesSrv.getLovedPosts();
        self.lovePostsIds = [];
        angular.forEach(self.cookieObj, function (key, val) {
            self.lovePostsIds.push(key);
        });

        postsSrv.getPostsByIds(self.lovePostsIds).then(function (response) {
            console.log(response.data);
            self.posts = response.data;

            self.cookieObj = cookiesSrv.getLovedPosts();
            angular.forEach(self.posts, (function (post) {
                post['love'] = self.cookieObj.hasOwnProperty(post.id);
            }));
        });

        self.love = function(postToLove) {
            postToLove.love = !postToLove.love;
            if(postToLove.love){
                cookiesSrv.addLovedPost(postToLove.id);
            }
            else {
                cookiesSrv.removeLovedPost(postToLove.id)
            }
        };
    }
})();
