(function(){
    "use strict";

    angular.module('myApp').controller('postsCtrl', ["$scope", "$routeParams", "$location", "$log", "postsSrv",
        "cookiesSrv", postsCtrl]);

    function postsCtrl ($scope, $routeParams, $location, $log, postsSrv, cookiesSrv) {
        var self = this;
        self.postsPerPage = 50;
        var reqParams = $location.search();
        self.categoryId = $routeParams['categoryId'];

        self.lovePostsIds = cookiesSrv.getLovedPosts();
        postsSrv.getPostsByCategory(self.categoryId, reqParams).then(function (response) {
            //console.log(response.data);
            self.posts = response.data;

            angular.forEach(self.posts, (function (post) {
                post['love'] = self.lovePostsIds.indexOf(post.id) !== -1;
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

        self.pagination = {
            backButtonDisabled: function () {
                return !reqParams.hasOwnProperty('page') || reqParams['page'] === "1";
            },
            forwardButtonDisabled: function () {
                return self.posts !== undefined && self.posts.length !== self.postsPerPage;
            },
            back: function () {
                if (!self.pagination.backButtonDisabled()) {
                    reqParams['page'] = parseInt(reqParams['page']) - 1;
                    $location.path($location.path()).search(reqParams);
                }
            },
            forward: function () {
                if (!self.pagination.forwardButtonDisabled()) {
                    if (!reqParams.hasOwnProperty('page'))
                        reqParams['page'] = 1;
                    reqParams['page'] = parseInt(reqParams['page']) + 1;
                    $location.path($location.path()).search(reqParams);
                }
            }
        };
    }
})();
