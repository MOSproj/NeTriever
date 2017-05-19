(function(){
    "use strict";

    angular.module('myApp').controller('lovesCtrl', ["$scope", "$routeParams", "$location", "$log", "postsSrv",
        "cookiesSrv", lovesCtrl]);

    function lovesCtrl ($scope, $routeParams, $location, $log, postsSrv, cookiesSrv) {
        var self = this;
        var reqParams = $location.search();

        self.lovePostsIds = cookiesSrv.getLovedPosts();
        console.log(self.lovePostsIds);

        if(self.lovePostsIds.length > 0) {
            postsSrv.getPostsByIds(self.lovePostsIds).then(function (response) {
                console.log(response.data);
                self.posts = response.data;

                angular.forEach(self.posts, (function (post) {
                    post['love'] = self.lovePostsIds.indexOf(post.id) !== -1;
                }));
            });
        }
        else {
            self.posts = [];
        }

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
