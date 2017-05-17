(function(){
    "use strict";

    angular.module('myApp').factory("cookiesSrv", ["$http", "$cookies", "$log" , cookiesSrv]);

    function cookiesSrv($http, $cookies, $log){
        return {
            getLovedPosts: function(){
                var cookieObj = $cookies.getObject('lovedPosts');
                if(cookieObj !== undefined)
                    return cookieObj;
                else {
                    $cookies.putObject('lovedPosts', {});
                    return $cookies.getObject('lovedPosts');
                }
            },
            addLovedPost: function(postId){
                var cookieObj = $cookies.getObject('lovedPosts');
                if(!cookieObj.hasOwnProperty(postId)) {
                    cookieObj[postId] = postId;
                    $cookies.putObject('lovedPosts', cookieObj);
                }
                return cookieObj;
            },
            removeLovedPost: function(postId){
                var cookieObj = $cookies.getObject('lovedPosts');
                if(cookieObj.hasOwnProperty(postId)) {
                    delete cookieObj[postId];
                    $cookies.putObject('lovedPosts', cookieObj);
                }
                return cookieObj;
            },
            removeAllLovedPost: function(){
                $cookies.remove('lovedPosts');
                return {};
            }
        };
    }
})();
