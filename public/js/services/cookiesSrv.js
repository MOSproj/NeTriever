(function(){
    "use strict";

    angular.module('myApp').factory("cookiesSrv", ["$http", "$cookies", "$log" , cookiesSrv]);

    function cookiesSrv($http, $cookies, $log){
        return {
            getLovedPosts: function(){
                var cookieObj = $cookies.getObject('lovedPosts');
                if(cookieObj !== undefined && angular.isArray(cookieObj))
                    return cookieObj;
                else {
                    $cookies.putObject('lovedPosts', []);
                    return [];
                }
            },
            addLovedPost: function(postId){
                var cookieObj = $cookies.getObject('lovedPosts');
                if(cookieObj.indexOf(postId) === -1) {
                    cookieObj.push(postId);
                    $cookies.putObject('lovedPosts', cookieObj);
                }
                return cookieObj;
            },
            removeLovedPost: function(postId){
                var cookieObj = $cookies.getObject('lovedPosts');
                var index = cookieObj.indexOf(postId);
                if(index !== -1) {
                    cookieObj.splice(index, 1);
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
